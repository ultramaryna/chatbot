# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from random import randrange, choice
import codecs, re
from operator import itemgetter

from .answers import *
from .questions import *
from .assignation import *
from .data import *

class Test(models.Model):
    napis_text = models.CharField(max_length=200)
    data_date = models.DateTimeField('date published')

class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_lat = models.CharField(max_length=30, default='')
    user_lon = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.user_name

    def publish(self):
        self.save()

class Chat(models.Model):
    #message_list
    message_text = models.CharField(max_length=300)
    message_date = models.DateTimeField(default=timezone.now)
    message_author = models.CharField(max_length=1, default='B')
    message_gif = models.CharField(max_length=200, default='')
    weather_temp = models.CharField(max_length=8, default='')
    weather_temp_min = models.CharField(max_length=8, default='')
    weather_humidity = models.CharField(max_length=8, default='')
    weather_wind = models.CharField(max_length=20, default='')
    weather_pressure = models.CharField(max_length=20, default='')
    weather_img = models.CharField(max_length=50, default='')
    weather_place = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.message_text

    def publish(self):
        self.published_date = timezone.now()
        self.message_author = 'U'
        self.save()

############################################################################

    def bot_welcome(self, name):
        possible_answers = answers['welcome']
        random_answer = choice(possible_answers)
        if '{name}' in random_answer:
            random_answer = random_answer.replace('{name}', name)
        self.message_text = random_answer

        possible_gifs = gifs['welcome']
        random_gif = choice(possible_gifs)
        self.message_gif = random_gif

        self.published_date = timezone.now()
        self.save()

##################################################################

    def bot_respond(self, message, name, lat, lon):
        response_type = self._match_response_type(query=message)
        data = {}
        if lat and lon:
            data = get_nearest_data(lat, lon)
            weather_data = get_nearest_weather(lat, lon)
            print(weather_data)

        #Przydziela typ odpowiedzi na podstawie stanu powietrza
        if response_type == 'if_smog':
            if not data:
                response_type = 'no_data'
            else:
                response_type = response_type+'_'+str(data['pollutionLevel'])

        if response_type == 'if_rain':
            icon = weather_data['weather'][0]['icon']
            if icon is '09d' or '09n':
                response_type = response_type+'_rain'
            elif icon is '10d' or '10n':
                response_type = response_type+'_chancerain'
            elif icon is '13d' or '13n':
                response_type = response_type+'_snow'
            else:
                response_type = response_type+'_no'

        if response_type == "weather":
            temp = weather_data['main']['temp']
            self.weather_temp = str(round(temp-273.15))
            temp_min = weather_data['main']['temp_min']
            self.weather_temp_min = str(round(temp_min-273.15))
            self.weather_humidity = str(weather_data['main']['humidity'])
            self.weather_wind = str(weather_data['wind']['speed'])
            self.weather_pressure = str(weather_data['main']['pressure'])
            img = str(weather_data['weather'][0]['icon'])
            self.weather_img = str(images[img][0])
            self.weather_place = str(weather_data['name'])
            self.message_text = 'weather'

        else:

            possible_answers = answers[response_type]
            random_answer = choice(possible_answers)
            #Podmienia fragmenty odpowiedzi na zmienne
            if '{name}' in random_answer:
                random_answer = random_answer.replace('{name}', name)
            if '{sensor}' in random_answer:
                place = data['address']['locality']+', '+data['address']['route']
                random_answer = random_answer.replace('{sensor}', place)
            if '{temperature}' in random_answer:
                temp = weather_data['main']['temp']
                temp = str(round(temp-273.15))
                random_answer = random_answer.replace('{temperature}', temp)
            if '{pressure}' in random_answer:
                pressure = str(weather_data['main']['pressure'])
                random_answer = random_answer.replace('{pressure}', pressure)
            self.message_text = random_answer

            if response_type in gifs:
                possible_gifs = gifs[response_type]
                random_gif = choice(possible_gifs)
                self.message_gif = random_gif


        self.published_date = timezone.now()
        self.save()


##################################################################
    def _match_response_type(self, query):
        print(type(query))

        words = self._words_from_line(line=query)

        #words = words.encode('UTF-8')
        #print('words are')
        #print(words)

        ranking = []

        for key, value in messages.items():
            points = 0
            length = len(value)
            #print('length ' + str(length))
            # print('question number ' + key)
            for element in value:
                if element[0] == '^':
                    if element[1:] in words:
                        # print('yeah +1 point for optional word:' + element)
                        points+=1
                    else:
                        length-=1
                else:
                    if element in words:
                        # print('yeah +1 point for word:' + element)
                        points+=1
            #print('length ' + str(length))
            if (length == len(words)) and (points != 0):
                points+=1
            score = points/length
            ranking.append((key, score))
            # print(' len value =' + str(length))
            # print('append' + key + ':' + str(score))
            # print('')
            # print('')


        ranking.sort(key = itemgetter(1), reverse = True)
        #print('ranking')
        #print(ranking)
        if ranking[0][1] < 0.29:
            question_id = 0
        else:
            question_id = ranking[0][0]
        #print('question_id ==')
        #print(question_id)

        for key, value in assignation.items():
            for element in value:
                if element == question_id:
                    response_type = key
                    #print('yeah')

        return response_type


    def _words_from_line(self, line):
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split('[\W]+', line)
        #words = re.split('[\W\d]+', line)
        return [w.lower() for w in words if w]
