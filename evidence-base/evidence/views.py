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
from django.db.models import Count, Avg, IntegerField, F
#from django.db import IntegrityError

from django.views import generic
from evidence.models import Evidence, Analysis, Category
from . import models
from . import forms
from .forms import AnalysisForm

from braces.views import SelectRelatedMixin
from django.utils.timesince import timesince

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
        ).annotate(
        cr1_avg=Avg('analysis__content_rating_1', output_field=IntegerField()),
        cr2_avg=Avg('analysis__content_rating_2', output_field=IntegerField()),
        cr3_avg=Avg('analysis__content_rating_3', output_field=IntegerField()),
        cr4_avg=Avg('analysis__content_rating_4', output_field=IntegerField()),
        cr5_avg=Avg('analysis__content_rating_5', output_field=IntegerField()),
        sr1_avg=Avg('analysis__source_rating_1', output_field=IntegerField()),
        sr2_avg=Avg('analysis__source_rating_2', output_field=IntegerField()),
        sr3_avg=Avg('analysis__source_rating_3', output_field=IntegerField()),
        sr4_avg=Avg('analysis__source_rating_4', output_field=IntegerField()),
        sr5_avg=Avg('analysis__source_rating_5', output_field=IntegerField()),
        ).annotate(
        suwr=(F('category__attribute__board__content_rating_1_weight')*F('cr1_avg'))+
        (F('category__attribute__board__content_rating_2_weight')*F('cr2_avg'))+
        (F('category__attribute__board__content_rating_3_weight')*F('cr3_avg'))+
        (F('category__attribute__board__content_rating_4_weight')*F('cr4_avg'))+
        (F('category__attribute__board__content_rating_5_weight')*F('cr5_avg'))+
        (F('category__attribute__board__source_rating_1_weight')*F('sr1_avg'))+
        (F('category__attribute__board__source_rating_2_weight')*F('sr2_avg'))+
        (F('category__attribute__board__source_rating_3_weight')*F('sr3_avg'))+
        (F('category__attribute__board__source_rating_4_weight')*F('sr4_avg'))+
        (F('category__attribute__board__source_rating_5_weight')*F('sr5_avg'))
        ).annotate(
        smvc=(F('category__attribute__board__content_rating_1_weight')*5)+
        (F('category__attribute__board__content_rating_2_weight')*5)+
        (F('category__attribute__board__content_rating_3_weight')*5)+
        (F('category__attribute__board__content_rating_4_weight')*5)+
        (F('category__attribute__board__content_rating_5_weight')*5)+
        (F('category__attribute__board__source_rating_1_weight')*5)+
        (F('category__attribute__board__source_rating_2_weight')*5)+
        (F('category__attribute__board__source_rating_3_weight')*5)+
        (F('category__attribute__board__source_rating_4_weight')*5)+
        (F('category__attribute__board__source_rating_5_weight')*5)
        ).annotate(
        evr=(
        ((F('suwr') / F('smvc')) *100)/20))

#This view updates a single piece of evidence
class EvidenceUpdate(generic.UpdateView):
    model = models.Evidence
    fields = ['title','contributors_note','website','publisher','publication_date','content_type','research_type','category']
    template_name_suffix = '_update_form'

class EvidenceDelete(generic.DeleteView):
    model = Evidence
#    success_url = reverse_lazy('evidence:filtered_evidence')
# Will resolve success url after user flow is complete


#This view is used to add analysis to a piece of evidence
def add_analysis_to_evidence(request, pk):
    evidence = get_object_or_404(Evidence, pk=pk)
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.evidence = evidence
            analysis.analyst  = request.user
            analysis.save()
            return redirect("evidence:single", username=evidence.user, pk=evidence.pk)
    else:
        analysis_form = AnalysisForm()
    return render(request, 'evidence/add_analysis_to_evidence.html', {'analysis_form': analysis_form})
