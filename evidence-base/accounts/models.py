from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# Create your models here.

#Please ignore this model. It is a legacy from my training wheels.
#It's largely harmless but I couldn't delete it without wrecking the db.
class LameUser(auth.models.User, auth.models.PermissionsMixin):
    #This is to create a string representation of the user.
    def __str__(self):
        return "@{}".format(self.username)

class Tags(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_tag = models.ForeignKey('self', null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    related_name='userprofile')
    first_name = models.CharField(max_length=150, null=True, default='')
    last_name = models.CharField(max_length=150, null=True, default='')
    description = models.CharField(max_length=150, default='')
    profile_picture = models.ImageField(upload_to='profile_image', blank=True)
    website = models.URLField(blank=True, null=True)
    organisation = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    current_position = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    interests =  models.ManyToManyField(Tags, blank=True, related_name='UserProfile')
    publications = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    associations = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    skills = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    certifications = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    languages = models.CharField(max_length=150, unique=False, blank=True,
    null=True, default='')
    slug = models.SlugField(allow_unicode=True, unique=True, default=User)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "accounts:viewprofile",
            kwargs={
                "slug": self.slug
            }
        )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
