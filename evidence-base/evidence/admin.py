from django.contrib import admin

from . import models
from evidence.models import Evidence, Analysis

# Register your models here.
admin.site.register(models.Evidence)
admin.site.register(models.Analysis)
