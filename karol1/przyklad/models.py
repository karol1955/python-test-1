from django.db import models

# Create your models here.
class Pomysl(models.Model):
    nazwa = models.CharField(max_length=100)
    tresc = models.TextField()
    rodzaj = models.PositiveSmallIntegerField(
        default=0,
        choices=[
            (0, "zwykly"),
            (1, "fajny"),
            (2, "superowy")
        ]
    )