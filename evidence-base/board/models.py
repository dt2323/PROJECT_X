from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse

import misaka
from django.contrib.auth import get_user_model
Current_user = get_user_model()

# Models from our applications here


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100, unique=False, blank=False)
    sub_title = models.CharField(max_length=100, blank=False)
    attribute_description = models.TextField(max_length=300, blank=False)

    user = models.ForeignKey(Current_user, related_name="board")
    created_at = models.DateTimeField(auto_now_add=True)


    content_rating_1_title = models.CharField(max_length=50, default="Content Characterstic 1")
    content_rating_1_weight = models.IntegerField(default=3)
    content_rating_2_title = models.CharField(max_length=50, default="Content Characterstic 2")
    content_rating_2_weight = models.IntegerField(default=3)
    content_rating_3_title = models.CharField(max_length=50, default="Content Characterstic 3")
    content_rating_3_weight = models.IntegerField(default=3)
    content_rating_4_title = models.CharField(max_length=50, default="Content Characterstic 4")
    content_rating_4_weight = models.IntegerField(default=3)
    content_rating_5_title = models.CharField(max_length=50, default="Content Characterstic 5")
    content_rating_5_weight = models.IntegerField(default=3)

    source_rating_1_title = models.CharField(max_length=50, default="Source Characterstic 1")
    source_rating_1_weight = models.IntegerField(default=3)
    source_rating_2_title = models.CharField(max_length=50, default="Source Characterstic 2")
    source_rating_2_weight = models.IntegerField(default=3)
    source_rating_3_title = models.CharField(max_length=50, default="Source Characterstic 3")
    source_rating_3_weight = models.IntegerField(default=3)
    source_rating_4_title = models.CharField(max_length=50, default="Source Characterstic 4")
    source_rating_4_weight = models.IntegerField(default=3)
    source_rating_5_title = models.CharField(max_length=50, default="Source Characterstic 5")
    source_rating_5_weight = models.IntegerField(default=3)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #If you need to do something
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "board:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
