from django.conf.urls import include, url
from . import views


urlpatterns = [
    url('create/', views.create_board, name='create_board'),
    url(r'^view/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.ViewBoard.as_view(), name='view_board'),
]
