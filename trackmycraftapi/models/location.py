from django.db import models
from django.db.models.deletion import CASCADE


class Location(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 10)
    zipcode = models.CharField(max_length = 5)
