from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import redirect

# from django.db import IntegrityError

from django.views import generic
from evidence.models import Evidence, Analysis
from . import models
from . import forms
from .forms import AnalysisForm

from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

# This view allows users to add evidence to a category
class CreateEvidence(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title', 'contributors_note', 'website', 'publisher', 'content_type', 'research_type', 'category')
    model = models.Evidence

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# This view is used to retrieve a single piece of evidence
class EvidenceDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Evidence
    select_related = ("category", "user")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


# This view updates a single piece of evidence
class EvidenceUpdate(generic.UpdateView):
    model = models.Evidence
    fields = ['title', 'contributors_note', 'website', 'publisher', 'publication_date', 'content_type', 'research_type',
              'category']
    template_name_suffix = '_update_form'


# This view lists evidence, filtered by category.
class EvidenceListFiltered(generic.ListView):
    model = Evidence
    select_related = ("category", "user")
    template_name = 'evidence/evidence_list.html'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug'])
        return qs


class EvidenceDelete(generic.DeleteView):
    model = Evidence


#    success_url = reverse_lazy('evidence:filtered_evidence')
# Will resolve success url after user flow is complete


# This view is used to add analysis to a piece of evidence
def add_analysis_to_evidence(request, pk):
    evidence = get_object_or_404(Evidence, pk=pk)
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.evidence = evidence
            analysis.analyst = request.user
            analysis.save()
            return redirect("evidence:single", username=evidence.user, pk=evidence.pk)
    else:
        analysis_form = AnalysisForm()
    return render(request, 'evidence/add_analysis_to_evidence.html', {'analysis_form': analysis_form})
