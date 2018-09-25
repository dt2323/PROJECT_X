from django.conf.urls import url

from . import views
from django.views.generic import ListView
#from evidence.views import EvidenceListFiltered
from django.db import models



app_name='evidence'

urlpatterns = [
    url(r"^$",views.CreateEvidence.as_view(), name="create_evidence"),
    url(r"(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.EvidenceDetail.as_view(),name="single"),
    url(r"(?P<pk>\d+)/analysis/$",views.add_analysis_to_evidence,name="add_analysis_to_evidence"),
    url(r"(?P<pk>\d+)/update/$",views.EvidenceUpdate.as_view(),name="evidence_update"),
#    url(r"(?P<slug>[-\w]+)/$",views.EvidenceListFiltered.as_view(),name="filtered_evidence"),
    url(r"(?P<pk>\d+)/delete/$",views.EvidenceDelete.as_view(),name="evidence_delete"),


#   url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
#   url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
#   url('evidence/new', views.CreateEvidence, name='create_evidence'),
#   url('evidence/<int:pk>/', views.EvidenceDetail, name='evidence_detail'),
]
