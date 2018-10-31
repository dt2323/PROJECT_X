from django.conf.urls import url

from . import views
from django.views.generic import ListView
#from evidence.views import EvidenceListFiltered
from django.db import models



app_name='evidence'

urlpatterns = [
    url(r"^(?P<slug>[-\w]+)/add-evidence/$",views.add_evidence_to_category, name="create_evidence"),
    url(r"^(?P<pk>\d+)/(?P<slug>[-\w]+)/$",views.EvidenceDetail.as_view(),name="single"),
    url(r"^(?P<pk>\d+)/add-analysis-to/(?P<slug>[-\w]+)/$",views.add_analysis_to_evidence,name="add_analysis_to_evidence"),
    url(r"^(?P<pk>\d+)/analysis-of/(?P<slug>[-\w]+)/$",views.AnalysisDetail.as_view(),name="view_analysis"),
    url(r"^update/(?P<pk>\d+)/(?P<username>[-\w]+)/(?P<slug>[-\w]+)/$",views.EvidenceUpdate.as_view(),name="evidence_update"),
    url(r"^delete/(?P<pk>\d+)/(?P<username>[-\w]+)/(?P<slug>[-\w]+)/delete-evidence/$",views.EvidenceDelete.as_view(),name="evidence_delete"),
    url(r"^delete/(?P<pk>\d+)/(?P<username>[-\w]+)/(?P<slug>[-\w]+)/delete-analysis/$",views.AnalysisDelete.as_view(),name="analysis_delete"),
    url(r"^(?P<pk>\d+)/analysis-update/(?P<slug>[-\w]+)/$",views.AnalysisUpdate.as_view(),name="update_analysis"),

#   url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
]
