from django.shortcuts import render

# Create your views here.
from django.db import models
from django.forms import ModelForm

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import datetime
import misaka
from django.contrib.auth import get_user_model
Current_user = get_user_model()
from django.db.models import Avg

# Models from our applications here
from category.models import Category



# Create your models here.
