from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UpdateProfileForm
from accounts.models import UserProfile
from . import models
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

from . import forms
# Create your views here.

#This is for creating a new user.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')#After succesful signup, we reverse them back to the login page so they can login.
    template_name = 'accounts/signup.html'

class ViewProfile(LoginRequiredMixin, DetailView):
    model = models.UserProfile
    template_name = 'accounts/userprofile_detail.html'

class CreateProfile(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = models.UserProfile
    select_related = ("user")
    fields = ('first_name', 'last_name', 'description', 'profile_picture',
    'website', 'organisation', 'current_position', 'interests', 'publications',
    'associations', 'skills', 'certifications', 'languages')
    success_url = reverse_lazy('viewprofile')
    template_name = 'accounts/createprofile.html'

class UpdateProfile(LoginRequiredMixin, SelectRelatedMixin, UpdateView):
    model = models.UserProfile
    form_class = UpdateProfileForm
    select_related = ("user",)
    template_name_suffix = '_update_form'
