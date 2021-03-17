from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Subscription(models.Model):
    follower_id = models.ForeignKey(
        "CraftUser",
        on_delete = CASCADE,
        related_name = "follower_subscriptions",
        related_query_name = "follower_subscription"
    )
    author_id = models.ForeignKey(
      "CraftUser",
      on_delete = CASCADE,
      related_name = "author_subscriptions",
      related_query_name = "author_subscription"
    )
    created_on = models.DateTimeField(auto_now_add = True)
    ended_on = models.DateTimeField(null = True)

    class Meta:
        unique_together = ("follower_id", "author_id")
