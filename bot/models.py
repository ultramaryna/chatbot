# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from random import randrange, choice
import codecs, re
from operator import itemgetter


from .answers import *
from .questions import *
from .assignation import *

#that doesn't work
#from clp3 import clp
#import questions, answers, assignation

# Create your models here.
class Test(models.Model):
    napis_text = models.CharField(max_length=200)
    data_date = models.DateTimeField('date published')

class User(models.Model):
    user_name = models.CharField(max_length=30)
    #user_location = ???

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
        name_xxx = "ZZZ"
        self.message_text = random_answer

        possible_gifs = gifs['welcome']
        random_gif = choice(possible_gifs)
        self.message_gif = random_gif

        self.published_date = timezone.now()
        self.save()

##################################################################

    def bot_respond(self, message):
        response_type = self._match_response_type(query=message)
        print(response_type)

        possible_answers = answers[response_type]
        random_answer = choice(possible_answers)
        self.message_text = random_answer

        if response_type in gifs:
            possible_gifs = gifs[response_type]
            random_gif = choice(possible_gifs)
            self.message_gif = random_gif

        self.published_date = timezone.now()
        self.save()


##################################################################
    def _match_response_type(self, query):
        words = self._words_from_line(line=query)

        print('words are')
        print(words)

        ranking = []

        for key, value in messages.items():
            points = 0
            length = len(value)
            print('length ' + str(length))
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
            print('length ' + str(length))
            if (length == len(words)) and (points != 0):
                points+=1
            score = points/length
            ranking.append((key, score))
            # print(' len value =' + str(length))
            # print('append' + key + ':' + str(score))
            # print('')
            # print('')


        ranking.sort(key = itemgetter(1), reverse = True)
        print('ranking')
        print(ranking)
        if ranking[0][1] < 0.29:
            question_id = 0
        else:
            question_id = ranking[0][0]
        print('question_id ==')
        print(question_id)

        for key, value in assignation.items():
            for element in value:
                if element == question_id:
                    response_type = key
                    print('yeah')

        return response_type


    def _words_from_line(self, line):
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split('[\W]+', line)
        #words = re.split('[\W\d]+', line)
        return [w.lower() for w in words if w]
