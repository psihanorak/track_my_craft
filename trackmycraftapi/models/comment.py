from django.db import models
from django.db.models.deletion import CASCADE


class Comment(models.Model):
    beer = models.ForeignKey(
        "Beer",
        on_delete = CASCADE,
        related_name = "beers",
        related_query_name = "beer",
        null = False,
        blank = True
    )
    author = models.ForeignKey(
        "CraftUser",
        on_delete = CASCADE,
        related_name = "craftusers",
        related_query_name = "craftuser"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
