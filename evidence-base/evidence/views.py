from django.shortcuts import render
from decimal import Decimal
import math

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
from django.db.models import Count, Avg, IntegerField, F, Q, Case, Value, When, DecimalField, ExpressionWrapper
#from django.db import IntegrityError

from django.views import generic
from evidence.models import Evidence, Analysis, Category
from . import models
from . import forms
from .forms import AnalysisForm, EvidenceForm

from braces.views import SelectRelatedMixin
from django.utils.timesince import timesince

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class CreateEvidence(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title','contributors_note','website','publisher','content_type','research_type','category')
    model = models.Evidence
    form = EvidenceForm()
    select_related = ("category")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

#This view allows users to add evidence to a category
def add_evidence_to_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = EvidenceForm(request.POST)
        if form.is_valid():
            evidence = form.save(commit=False)
            #evidence.category = category
            evidence.user  = request.user
            evidence.save()
            return redirect("evidence:single", pk=evidence.pk, slug=evidence.slug)
    else:
        evidence_form = EvidenceForm()
    return render(request, 'evidence/evidence_form.html', {'evidence_form': evidence_form,
    'category': category, 'slug': category.slug})



#This view is used to retrieve a single piece of evidence
class EvidenceDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Evidence
    select_related = ("category", "user")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            pk=self.kwargs.get("pk")
        ).annotate(#This annotates an avg of the individual ratings to the evidence object
        cr1_avg=Avg('analysis__content_rating_1',
        exclude=Q(analysis__content_rating_1__is_null=True, analysis__content_rating_1__is_lte=0)),
        cr2_avg=Avg('analysis__content_rating_2',
        exclude=Q(analysis__content_rating_2__is_null=True, analysis__content_rating_2__is_lte=0)),
        cr3_avg=Avg('analysis__content_rating_3',
        exclude=Q(analysis__content_rating_3__is_null=True, analysis__content_rating_3__is_lte=0)),
        cr4_avg=Avg('analysis__content_rating_4',
        exclude=Q(analysis__content_rating_4__is_null=True, analysis__content_rating_4__is_lte=0)),
        cr5_avg=Avg('analysis__content_rating_5',
        exclude=Q(analysis__content_rating_5__is_null=True, analysis__content_rating_5__is_lte=0)),
        sr1_avg=Avg('analysis__source_rating_1',
        exclude=Q(analysis__source_rating_1__is_null=True, analysis__source_rating_1__is_lte=0)),
        sr2_avg=Avg('analysis__source_rating_2',
        exclude=Q(analysis__source_rating_2__is_null=True, analysis__source_rating_2__is_lte=0)),
        sr3_avg=Avg('analysis__source_rating_3',
        exclude=Q(analysis__source_rating_3__is_null=True, analysis__source_rating_3__is_lte=0)),
        sr4_avg=Avg('analysis__source_rating_4',
        exclude=Q(analysis__source_rating_4__is_null=True, analysis__source_rating_4__is_lte=0)),
        sr5_avg=Avg('analysis__source_rating_5',
        exclude=Q(analysis__source_rating_5__is_null=True, analysis__source_rating_5__is_lte=0)),
        ).annotate(#This checks the avg values to ensure no null values are passed to suwr calculation
        cr1_avg_checked=Case(When(cr1_avg=None, then=Value(0)), When(cr1_avg__gt=0, then=F('cr1_avg')),
        default=Value(0), output_field=DecimalField()),
        cr2_avg_checked=Case(When(cr2_avg=None, then=Value(0)),When(cr2_avg__gt=0, then=F('cr2_avg')),
        default=Value(0), output_field=DecimalField()),
        cr3_avg_checked=Case(When(cr3_avg=None, then=Value(0)), When(cr3_avg__gt=0, then=F('cr3_avg')),
        default=Value(0), output_field=DecimalField()),
        cr4_avg_checked=Case(When(cr4_avg=None, then=Value(0)), When(cr4_avg__gt=0, then=F('cr4_avg')),
        default=Value(0), output_field=DecimalField()),
        cr5_avg_checked=Case(When(cr5_avg=None, then=Value(0)), When(cr5_avg__gt=0, then=F('cr5_avg')),
        default=Value(0), output_field=DecimalField()),
        sr1_avg_checked=Case(When(sr1_avg=None, then=Value(0)), When(sr1_avg__gt=0, then=F('sr1_avg')),
        default=Value(0), output_field=DecimalField()),
        sr2_avg_checked=Case(When(sr2_avg=None, then=Value(0)), When(sr2_avg__gt=0, then=F('sr2_avg')),
        default=Value(0), output_field=DecimalField()),
        sr3_avg_checked=Case(When(sr3_avg=None, then=Value(0)), When(sr3_avg__gt=0, then=F('sr3_avg')),
        default=Value(0), output_field=DecimalField()),
        sr4_avg_checked=Case(When(sr4_avg=None, then=Value(0)),When(sr4_avg__gt=0, then=F('sr4_avg')),
        default=Value(0), output_field=DecimalField()),
        sr5_avg_checked=Case(When(sr5_avg=None, then=Value(0)), When(sr5_avg__gt=0, then=F('sr5_avg')),
        default=Value(0), output_field=DecimalField()),
        ).annotate(suwr=ExpressionWrapper(#This annotates the suwr(sum of user weighted-ratings) from board settings to the evidence object
        (F('category__attribute__board__content_rating_1_weight')*Decimal('1.0')*F('cr1_avg_checked'))+
        (F('category__attribute__board__content_rating_2_weight')*Decimal('1.0')*F('cr2_avg_checked'))+
        (F('category__attribute__board__content_rating_3_weight')*Decimal('1.0')*F('cr3_avg_checked'))+
        (F('category__attribute__board__content_rating_4_weight')*Decimal('1.0')*F('cr4_avg_checked'))+
        (F('category__attribute__board__content_rating_5_weight')*Decimal('1.0')*F('cr5_avg_checked'))+
        (F('category__attribute__board__source_rating_1_weight')*Decimal('1.0')*F('sr1_avg_checked'))+
        (F('category__attribute__board__source_rating_2_weight')*Decimal('1.0')*F('sr2_avg_checked'))+
        (F('category__attribute__board__source_rating_3_weight')*Decimal('1.0')*F('sr3_avg_checked'))+
        (F('category__attribute__board__source_rating_4_weight')*Decimal('1.0')*F('sr4_avg_checked'))+
        (F('category__attribute__board__source_rating_5_weight')*Decimal('1.0')*F('sr5_avg_checked')),
        output_field=DecimalField()),
        ).annotate(#This annotates the highest possible score the evidence could have achieved given weights from board settings
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
    template_name_suffix = '_update_form'
    form_class = EvidenceForm
    success_url = reverse_lazy('evidence:single')

    def get_success_url(self):
        evidence_slug = self.object.slug
        evidence_pk = self.object.pk
        return reverse_lazy('evidence:single',
        kwargs={'pk': evidence_pk, 'slug': evidence_slug})


class EvidenceDelete(generic.DeleteView):
    model = Evidence
    success_url = reverse_lazy('category:filtered_evidence')

    def get_success_url(self):
        category_slug = self.object.category.slug
        return reverse_lazy('category:filtered_evidence', kwargs={'slug': category_slug})

#This view is used to add analysis to a piece of evidence
def add_analysis_to_evidence(request, pk, slug):
    evidence = get_object_or_404(Evidence, pk=pk, slug=slug)

    if request.method == "POST":
        form = AnalysisForm(request.POST)

        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.evidence = evidence
            analysis.analyst  = request.user
            if analysis.content_rating_1 == "0":
                analysis.content_rating_1 = None
            else:
                analysis.content_rating_1 = math.floor(int(analysis.content_rating_1)/10)
            if analysis.content_rating_2 == "0":
                analysis.content_rating_2 = None
            else:
                analysis.content_rating_2 = math.floor(int(analysis.content_rating_2)/10)
            if analysis.content_rating_3 == "0":
                analysis.content_rating_3 = None
            else:
                analysis.content_rating_3 = math.floor(int(analysis.content_rating_3)/10)
            if analysis.content_rating_4 == "0":
                analysis.content_rating_4 = None
            else:
                analysis.content_rating_4 = math.floor(int(analysis.content_rating_4)/10)
            if analysis.content_rating_5 == "0":
                analysis.content_rating_5 = None
            else:
                analysis.content_rating_5 = math.floor(int(analysis.content_rating_5)/10)

            if analysis.source_rating_1 == "0":
                analysis.source_rating_1 = None
            else:
                analysis.source_rating_1 = math.floor(int(analysis.source_rating_1)/10)
            if analysis.source_rating_2 == "0":
                analysis.source_rating_2 = None
            else:
                analysis.source_rating_2 = math.floor(int(analysis.source_rating_2)/10)
            if analysis.source_rating_3 == "0":
                analysis.source_rating_3 = None
            else:
                analysis.source_rating_3 = math.floor(int(analysis.source_rating_3)/10)
            if analysis.source_rating_4 == "0":
                analysis.source_rating_4 = None
            else:
                analysis.source_rating_4 = math.floor(int(analysis.source_rating_4)/10)
            if analysis.source_rating_5 == "0":
                analysis.source_rating_5 = None
            else:
                analysis.source_rating_5 = math.floor(int(analysis.source_rating_5)/10)

            analysis.save()
            return redirect("evidence:single", pk=evidence.pk, slug=evidence.slug)
    else:
        analysis_form = AnalysisForm()
    return render(request, 'evidence/add_analysis_to_evidence.html',
    {'analysis_form': analysis_form, 'evidence': evidence})

#This view is used to view a single analysis report
class AnalysisDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Analysis
    select_related = ("analyst", "evidence")
    template_name = 'evidence/view_analysis.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            pk=self.kwargs['pk']
        )

class AnalysisDelete(generic.DeleteView):
    model = Analysis
    success_url = reverse_lazy('evidence:single')

    def get_success_url(self):
        evidence_slug = self.object.evidence.slug
        evidece_pk = self.object.evidence.pk
        return reverse_lazy('evidence:single', kwargs={'slug': evidence_slug, 'pk': evidece_pk})

class AnalysisUpdate(generic.UpdateView):
    model = Analysis
    template_name_suffix = '_update_form'
    form_class = AnalysisForm
    success_url = reverse_lazy('evidence:view_analysis')

#    def get_initial_for_field(self, field, field_name):
#        if field == 'content_rating_1'
#            return
#        return

    def get_initial(self):
        initial = super(AnalysisUpdate, self).get_initial()

        initial['content_rating_1'] = int(self.object.content_rating_1*10)
        initial['content_rating_2'] = int(self.object.content_rating_2*10)
        initial['content_rating_3'] = int(self.object.content_rating_3*10)
        initial['content_rating_4'] = int(self.object.content_rating_4*10)
        initial['content_rating_5'] = int(self.object.content_rating_5*10)

        initial['source_rating_1'] = int(self.object.source_rating_1*10)
        initial['source_rating_2'] = int(self.object.source_rating_2*10)
        initial['source_rating_3'] = int(self.object.source_rating_3*10)
        initial['source_rating_4'] = int(self.object.source_rating_4*10)
        initial['source_rating_5'] = int(self.object.source_rating_5*10)

        return initial

    def form_valid(self, form):
        analysis = form.save(commit=False)
        if analysis.content_rating_1 == "0":
            analysis.content_rating_1 = None
        else:
            analysis.content_rating_1 = math.floor(int(analysis.content_rating_1)/10)
        if analysis.content_rating_2 == "0":
            analysis.content_rating_2 = None
        else:
            analysis.content_rating_2 = math.floor(int(analysis.content_rating_2)/10)
        if analysis.content_rating_3 == "0":
            analysis.content_rating_3 = None
        else:
            analysis.content_rating_3 = math.floor(int(analysis.content_rating_3)/10)
        if analysis.content_rating_4 == "0":
            analysis.content_rating_4 = None
        else:
            analysis.content_rating_4 = math.floor(int(analysis.content_rating_4)/10)
        if analysis.content_rating_5 == "0":
            analysis.content_rating_5 = None
        else:
            analysis.content_rating_5 = math.floor(int(analysis.content_rating_5)/10)

        if analysis.source_rating_1 == "0":
            analysis.source_rating_1 = None
        else:
            analysis.source_rating_1 = math.floor(int(analysis.source_rating_1)/10)
        if analysis.source_rating_2 == "0":
            analysis.source_rating_2 = None
        else:
            analysis.source_rating_2 = math.floor(int(analysis.source_rating_2)/10)
        if analysis.source_rating_3 == "0":
            analysis.source_rating_3 = None
        else:
            analysis.source_rating_3 = math.floor(int(analysis.source_rating_3)/10)
        if analysis.source_rating_4 == "0":
            analysis.source_rating_4 = None
        else:
            analysis.source_rating_4 = math.floor(int(analysis.source_rating_4)/10)
        if analysis.source_rating_5 == "0":
            analysis.source_rating_5 = None
        else:
            analysis.source_rating_5 = math.floor(int(analysis.source_rating_5)/10)

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        evidence_slug = self.object.evidence.slug
        analysis_pk = self.object.pk
        return reverse_lazy('evidence:view_analysis',
        kwargs={'pk': analysis_pk, 'slug': evidence_slug})
