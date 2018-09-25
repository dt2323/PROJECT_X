from django.conf.urls import include, url
from . import views


urlpatterns = [
    url('create/', views.add_board, name='create_board'),
    url('view/', views.view_board, name='view_board'),
]