from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    responded = models.ManyToManyField(Question, through='Response')

class Question(models.Model):
    questioner = models.ForeignKey(User)
    text = models.Charfield(max_length=200)

class Word(model.Model):
    text = models.CharField(max_length=20)

class Respnse(model.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    user = models.ForeignKey(Question, on_delete = models.CASCADE)
    word = models.ForeignKey(Word, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    rank = model.IntegerField()
