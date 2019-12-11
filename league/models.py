from django.db import models

class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    area = models.CharField(max_length=30)


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    tla = models.CharField(max_length=3)
    shortName = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    email = models.EmailField(blank=True, unique=True)
    code = models.CharField(max_length=3)


class Player(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    dateOfBirth = models.DateTimeField()
    countryOfBirth = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    team_id = models.IntegerField()