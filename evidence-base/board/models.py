from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

import misaka
from django.contrib.auth import get_user_model

Current_user = get_user_model()


# Models from our applications here

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100, unique=False, blank=False,
    verbose_name=('Board Title'))
    sub_title = models.CharField(max_length=100, blank=False)
    board_description = models.TextField(max_length=300, blank=False)
    slug = models.SlugField(allow_unicode=True, unique=False, max_length=160)
    user = models.ForeignKey(Current_user, related_name="board")
    created_at = models.DateTimeField(auto_now_add=True)

    content_rating_1_title = models.CharField(max_length=50, default="Content Characterstic 1")
    content_rating_1_weight = models.IntegerField(default=0, blank=True,
    null=True)

    content_rating_2_title = models.CharField(max_length=50, default="Content Characterstic 2")
    content_rating_2_weight = models.IntegerField(default=0, blank=True,
    null=True)

    content_rating_3_title = models.CharField(max_length=50, default="Content Characterstic 3")
    content_rating_3_weight = models.IntegerField(default=0, blank=True,
    null=True)

    content_rating_4_title = models.CharField(max_length=50, default="Content Characterstic 4")
    content_rating_4_weight = models.IntegerField(default=0, blank=True,
    null=True)

    content_rating_5_title = models.CharField(max_length=50, default="Content Characterstic 5")
    content_rating_5_weight = models.IntegerField(default=0, blank=True,
    null=True)

    source_rating_1_title = models.CharField(max_length=50, default="Source Characterstic 1")
    source_rating_1_weight = models.IntegerField(default=0, blank=True,
    null=True)

    source_rating_2_title = models.CharField(max_length=50, default="Source Characterstic 2")
    source_rating_2_weight = models.IntegerField(default=0, blank=True,
    null=True)

    source_rating_3_title = models.CharField(max_length=50, default="Source Characterstic 3")
    source_rating_3_weight = models.IntegerField(default=0, blank=True,
    null=True)

    source_rating_4_title = models.CharField(max_length=50, default="Source Characterstic 4")
    source_rating_4_weight = models.IntegerField(default=0, blank=True,
    null=True)

    source_rating_5_title = models.CharField(max_length=50, default="Source Characterstic 5")
    source_rating_5_weight = models.IntegerField(default=0, blank=True,
    null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "board:view_board",
            kwargs={
                "slug": self.slug,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
