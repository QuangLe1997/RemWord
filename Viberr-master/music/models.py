import random

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Topic(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=True)
    topic_title = models.CharField(max_length=500)
    topic_logo = models.FileField()

    def __str__(self):
        return self.topic_title


class Vocabulary(models.Model):
    vocabulary_title = models.CharField(max_length=45)
    type = models.IntegerField(blank=True, null=True)
    story = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    pronounce = models.CharField(max_length=20, blank=True, null=True)
    mean = models.CharField(max_length=20, blank=True, null=True)
    topic = models.ForeignKey(Topic, default=1, on_delete=models.CASCADE)
    num_true = models.IntegerField(blank=True, null=True, default=0)
    num_false = models.IntegerField(blank=True, null=True, default=0)
    rating = models.IntegerField(blank=True, null=True, default=0)
    num_show = models.IntegerField(blank=True, null=True, default=0)

    # voca = VocaManager()

    # class Meta:
    #     managed = False
    #     db_table = 'vocabulary'

    def __str__(self):
        return self.vocabulary_title


class Predict(models.Model):
    result = models.IntegerField(blank=True, null=True)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    predict_txt = models.CharField(max_length=30, blank=True, null=True)
    id_user = models.ForeignKey(User, default=1, on_delete=True)
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)


class Example(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=True)
    example_txt = models.CharField(max_length=45, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
