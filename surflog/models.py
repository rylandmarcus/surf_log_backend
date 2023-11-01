from django.db import models

# Create your models here.
class Surfsession(models.Model):
    board = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    spot = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    