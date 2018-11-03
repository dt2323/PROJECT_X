from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse
from decimal import Decimal
from django.db.models import Count, Avg, IntegerField, F, Q, Case, Value, When, DecimalField, FloatField, ExpressionWrapper, CharField, Sum
import misaka
from django.contrib.auth import get_user_model
Current_user = get_user_model()

# Models from our applications here
from attribute.models import Attribute


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=False, blank=False)
    sub_title = models.CharField(max_length=100, blank=False)
    category_description = models.TextField(max_length=300, blank=False)

    user = models.ForeignKey(Current_user, related_name="category")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=False, max_length=160)
    attribute = models.ForeignKey(Attribute, related_name="category",null=True, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #If you need to do something
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "category:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
