from django.conf.urls import include, url

from django.contrib import admin
from . import views

urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^', include('app.urls')),
               url(r'^$', views.HomePage.as_view(),name='home'),#This is the first homepage
               url(r'^accounts/', include('accounts.urls',namespace='accounts')),#This connects our accounts application to our main project by connecting the accounts namespace to our accounts url
               url(r'^accounts/', include('django.contrib.auth.urls')),#This connects the authorisation tools that Django has in the backend
               url(r'^test/$',views.TestPage.as_view(),name='test'),
               url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
               url(r'^evidence/', include('evidence.urls'),name='evidence'),
               url(r'^category/', include('category.urls'),name='category'),

               ]
