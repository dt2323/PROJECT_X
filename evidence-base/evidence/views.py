from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from django.db.models import Count, Avg, IntegerField
#from django.db import IntegrityError

from django.views import generic
from evidence.models import Evidence, Analysis
from . import models
from . import forms
#from .forms import AnalysisForm

from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

#This view allows users to add evidence to a category
class CreateEvidence(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title','contributors_note','website','publisher','content_type','research_type','category')
    model = models.Evidence

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


#This view is used to retrieve a single piece of evidence
class EvidenceDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Evidence
    select_related = ("category", "user")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        ).annotate(cr1_avg=Avg('analysis__content_rating_1', output_field=IntegerField()),
        cr2_avg=Avg('analysis__content_rating_2', output_field=IntegerField()),
        cr3_avg=Avg('analysis__content_rating_3', output_field=IntegerField()),
        cr4_avg=Avg('analysis__content_rating_4', output_field=IntegerField()),
        cr5_avg=Avg('analysis__content_rating_5', output_field=IntegerField()),
        sr1_avg=Avg('analysis__source_rating_1', output_field=IntegerField()),
        sr2_avg=Avg('analysis__source_rating_2', output_field=IntegerField()),
        sr3_avg=Avg('analysis__source_rating_3', output_field=IntegerField()),
        sr4_avg=Avg('analysis__source_rating_4', output_field=IntegerField()),
        sr5_avg=Avg('analysis__source_rating_5', output_field=IntegerField()),
        )

#This view updates a single piece of evidence
class EvidenceUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Evidence
    fields = ['title','contributors_note','website','publisher','publication_date','content_type','research_type','category']
    template_name_suffix = '_update_form'


#This view deletes evidence.
class EvidenceDelete(LoginRequiredMixin, generic.DeleteView):
    model = Evidence
#    success_url = reverse_lazy('evidence:filtered_evidence')
# Will resolve success url after user flow is complete


#This view is used to add analysis to a piece of evidence
class AddAnalysis(generic.CreateView):
    model = Analysis
    fields = ['title', 'content_rating_1', 'content_rating_1_comment', 'content_rating_2', 'content_rating_2_comment', 'content_rating_3', 'content_rating_3_comment','content_rating_4', 'content_rating_4_comment','content_rating_5', 'content_rating_5_comment',
    'source_rating_1', 'source_rating_1_comment','source_rating_2', 'source_rating_2_comment',
    'source_rating_3', 'source_rating_3_comment','source_rating_4', 'source_rating_4_comment','source_rating_5', 'source_rating_5_comment']
    success_url = '/evidence/'

    def get_initial(self):
        evidence = get_object_or_404(Evidence, pk=self.kwargs.get('pk'))

        return {
            'evidence':evidence,
        }

    def form_valid(self, form):
        evidence = get_object_or_404(Evidence, pk=self.kwargs.get('pk'))
        form.instance.analyst = self.request.user
        form.instance.evidence = evidence
        res = super().form_valid(form)
        return redirect("evidence:single", username=evidence.user, pk=evidence.pk)

    def get_context_data(self, **kwargs):
        context = super(AddAnalysis, self).get_context_data(**kwargs)
        context['evidence'] = Evidence.objects.all().filter(pk=self.kwargs['pk'])
        return context
