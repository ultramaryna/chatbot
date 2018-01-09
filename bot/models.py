from django.db import models

#that doesn't work
#from clp3 import clp
#import questions, answers, assignation

# Create your models here.
class Test(models.Model):
    napis_text = models.CharField(max_length=200)
    data_date = models.DateTimeField('date published')

class Chat(models.Model):
    user_name = models.CharField(max_length=30)
    #local
    #message_list

    def __str__(self):
        return self.user_name

    def _get_message(self, message):
        words = self._words_from_line(message)
        words_ids = []
        for word in words:
            words_ids.append(str(clp(word)[0]))
        for question in questions.messages:
            if question[1] == words_ids:
                question_id = question[0]
        for group in assignation.groups:
            if group[1] in question_id:
                response_type = group[0]
        #
        #check with questions ____
        #
        #response = answers.description[word_label[0]][w]  coś takiego

        #return response

    def _get_random_response(response_type):
        response = answers.answers[response_type]


    def _words_from_line(line):
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split('[\W\d]+', line)
        return [w.lower() for w in words if w]
