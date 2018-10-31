from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts import models
from accounts.models import UserProfile

#Inheriting UserCreationForm from auth, this class helps forms create our users.
class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    #This is so we can have custom labels on the above form
    #(not necessary unless you need something custom)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name' #A custom label for username
        self.fields['email'].label = 'Email Address'

#WIP - Trying to add styling to the form
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ('first_name', 'last_name', 'description', 'profile_picture',
        'website', 'organisation', 'current_position', 'interests', 'publications',
        'associations', 'skills', 'certifications', 'languages')

        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'website':forms.TextInput(attrs={'class':'form-control'}),
        'organisation':forms.TextInput(attrs={'class':'form-control'}),
        'current_position':forms.TextInput(attrs={'class':'form-control'}),
        'publications':forms.Textarea(attrs={'class':'form-control'}),
        'associations':forms.TextInput(attrs={'class':'form-control'}),
        'skills':forms.TextInput(attrs={'class':'form-control'}),
        'certifications':forms.TextInput(attrs={'class':'form-control'}),
        'languages':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),

        }
