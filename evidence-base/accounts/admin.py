from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import Tags
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tags)
