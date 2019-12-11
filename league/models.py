from django.db import models

class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    area = models.CharField(max_length=50)


class Team(models.Model):
    name = models.CharField(max_length=50)
    tla = models.CharField(max_length=3)
    shortName = models.CharField(max_length=30)
    area = models.CharField(max_length=50)
    email = models.EmailField(blank=True, unique=True)
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE,
        default=None)