from django.conf.urls import url

from . import views
from django.views.generic import ListView
from evidence.views import EvidenceListFiltered


app_name='category'

urlpatterns = [

#    url(r"^category/([\w-]+)/$",views.EvidenceListFiltered.as_view(),name="filtered_evidence"),

]
