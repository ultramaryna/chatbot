from django.db import models

# Create your models here.
class Test(models.Model):
    napis_text = models.CharField(max_length=200)
    data_date = models.DateTimeField('date published')
