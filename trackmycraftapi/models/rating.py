from django.db import models


class Rating(models.Model):
    rating = models.CharField(max_length = 5)
