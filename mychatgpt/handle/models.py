from django.db import models

# Create your models here.
class Question(models.Model):
    ques=models.CharField(max_length=1000)
    