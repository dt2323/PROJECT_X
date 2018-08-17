from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

#This is for creating a new user.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')#After succesful signup, we reverse them back to the login page so they can login.
    template_name = 'accounts/signup.html'
