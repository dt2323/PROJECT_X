from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import datetime
import misaka
from django.contrib.auth import get_user_model
from django.db.models import Count, Avg, IntegerField, F
Current_user = get_user_model()

# Models from our applications here
from category.models import Category

# Create your models here.
class Evidence(models.Model):
    title = models.CharField(max_length=150, unique=False, blank=False)
    contributors_note = models.TextField(max_length=300, blank=False)
    website = models.URLField()
    publisher = models.CharField(max_length=250, unique=False)
    publication_date = models.DateField(default=datetime.date.today)
    slug = models.SlugField(allow_unicode=True, unique=False, max_length=160)

    content_type = models.CharField(max_length=100, unique=False, blank=True,
    null=True)# In this field user's define the type of content (blog, newspaper article, publication etc)
    research_type = models.CharField(max_length=100, unique=False, blank=True,
    null=True)# In this field user's define whether the research is based on primary or secondary research
    user = models.ForeignKey(Current_user, related_name="evidence")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name="evidence",null=True, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "evidence:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]


class Analysis(models.Model):
    title = models.CharField(max_length=150, unique=False, blank=False)
    evidence = models.ForeignKey('evidence.Evidence', on_delete=models.CASCADE, related_name='analysis')
    analyst = models.ForeignKey(Current_user, null=True, blank=True, related_name="analysis")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)


    key_finding1 = models.TextField(max_length=300, blank=True,
    null=True)
    key_finding2 = models.TextField(max_length=300, blank=True,
    null=True)
    key_finding3 = models.TextField(max_length=300, blank=True,
    null=True)

    ratings_range = (
    ('0', 'No Input'),
    ('1', 'Very Weak'),
    ('2', 'Weak'),
    ('3', 'Moderate'),
    ('4', 'Strong'),
    ('5', 'Very Strong'),
    )

    content_rating_1 = models.IntegerField(blank=True,
    null=True, default="0")
    content_rating_1_comment = models.TextField(max_length=300, blank=True,
    null=True)
    content_rating_2 = models.IntegerField(blank=True,
    null=True, default="0")
    content_rating_2_comment = models.TextField(max_length=300, blank=True,
    null=True)
    content_rating_3 = models.IntegerField(blank=True,
    null=True, default="0")
    content_rating_3_comment = models.TextField(max_length=300, blank=True,
    null=True)
    content_rating_4 = models.IntegerField(blank=True,
    null=True, default="0")
    content_rating_4_comment = models.TextField(max_length=300, blank=True,
    null=True)
    content_rating_5 = models.IntegerField(blank=True,
    null=True, default="0")
    content_rating_5_comment = models.TextField(max_length=300, blank=True,
    null=True)

    source_rating_1 = models.IntegerField(blank=True,
    null=True, default="0")
    source_rating_1_comment = models.TextField(max_length=300, blank=True,
    null=True)
    source_rating_2 = models.IntegerField(blank=True,
    null=True, default="0")
    source_rating_2_comment = models.TextField(max_length=300, blank=True,
    null=True)
    source_rating_3 = models.IntegerField(blank=True,
    null=True, default="0")
    source_rating_3_comment = models.TextField(max_length=300, blank=True,
    null=True)
    source_rating_4 = models.IntegerField(blank=True,
    null=True, default="0")
    source_rating_4_comment = models.TextField(max_length=300, blank=True,
    null=True)
    source_rating_5 = models.IntegerField(blank=True,
    null=True, default="0")
    source_rating_5_comment = models.TextField(max_length=300, blank=True,
    null=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.title



    class Meta:
        ordering = ["-created_at"]
