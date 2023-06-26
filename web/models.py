from django.db import models


class Slide(models.Model):
    header = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    image = models.CharField(max_length=128)


class Service(models.Model):
    header = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    image = models.CharField(max_length=128)


class Condition(models.Model):
    question = models.CharField(max_length=64)
    answer = models.CharField(max_length=512)
