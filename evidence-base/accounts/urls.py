from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),#This is our loged in view, we call LoginView from that authorisation as a view and then pass in our template.
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),#This doesn't need a template as django provides a default logged out view
    url(r'signup/$',views.SignUp.as_view(),name='signup')

]
