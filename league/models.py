from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    area = models.CharField(max_length=50)
