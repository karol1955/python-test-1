from django.db import models

# Create your models here.
class Pomysl(models.Model):
    nazwa = models.CharField(max_length=100)
    tresc = models.TextField()