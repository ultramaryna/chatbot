from django.db import models

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
