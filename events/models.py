from django.db import models

# Create your models here.


class Event(models.Model):
    header = models.CharField(max_length=64)
    content = models.CharField(max_length=1000)
    is_visible = models.BinaryField()
    is_removed = models.BinaryField()
    link = models.CharField(max_length=128)
