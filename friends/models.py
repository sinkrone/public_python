from django.db import models

# Create your models here.


class Friend(models.Model):
    header = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    link = models.CharField(max_length=128)
