from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse

import misaka
from django.contrib.auth import get_user_model
Current_user = get_user_model()

# Models from our applications here
from board.models import Board

# Create your models here.
class Attribute(models.Model):
    title = models.CharField(max_length=100, unique=False, blank=False)
    sub_title = models.CharField(max_length=100, blank=False)
    attribute_description = models.TextField(max_length=300, blank=False)

    user = models.ForeignKey(Current_user, related_name="attribute")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #If you need to do something
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "attribute:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
