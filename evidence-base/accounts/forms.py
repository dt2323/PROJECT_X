from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#Inheriting UserCreationForm from auth, this class helps forms create our users.
class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')#These are from contrib.auth but we're selecting which fields we want users to input.
        model = get_user_model()

    #This is so we can have custom labels on the above form (not necessary unless you need something custom)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name' #A custom label for username
        self.fields['email'].label = 'Email Address'
