from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Beer(models.Model):
    craftuser = models.ForeignKey(
        "CraftUser",
        on_delete = CASCADE,
        related_name = "beers",
        related_query_name = "beer"
    )
    category = models.ForeignKey(
        "Category",
        on_delete = SET_NULL,
        related_name = "beers",
        related_query_name = "beer",
        null = True,
        blank = True
    )
    types = models.CharField(max_length = 80)
    image_url = models.CharField(max_length = 255)
    rating = models.ManyToManyField(
        "Rating",
        related_name = "beer_ratings",
        related_query_name = "beer_rating"
    )
    location = models.ManyToManyField(
        "Location",
        related_name = "beer_locations",
        related_query_name = "beer_location"
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name = "tag_beers",
        related_query_name = "tag_beer"
    )
