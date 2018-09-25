from django.conf.urls import include, url
from . import views
from django.views.generic import ListView

urlpatterns = [
    url('board/', views.view_category_board, name='board'),
    url(r"^(?P<slug>[-\w]+)/$",views.EvidenceListFiltered.as_view(),name="filtered_evidence"),
]
