from __future__ import unicode_literals
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from evidence.models import Evidence, Analysis
from django.views import generic
from django.db.models import Count, Avg, IntegerField, F, Q, Case, Value, When, DecimalField, FloatField, ExpressionWrapper, CharField
from django.utils.timesince import timesince


from category.models import Category
from evidence.models import Evidence

#This view lists evidence, filtered by category.
class EvidenceListFiltered(generic.ListView):
    model = Evidence
    select_related = ("category", "user")
    template_name = 'category/view_category.html'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug']).annotate(#This annotates an avg of the individual ratings to the evidence object
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


        return qs

    def get_context_data(self, **kwargs):
        context = super(EvidenceListFiltered, self).get_context_data(**kwargs)
        context['category'] = Category.objects.filter(slug=self.kwargs['slug'])

        context['evidence_stats'] = Evidence.objects.filter(category__slug=self.kwargs['slug']).annotate(
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
        ).filter(suwr__gt=0).annotate(#This filter makes sure we only keep evidence objects that have analyses in the queryset
        evr=(((F('suwr') / F('smvc')) *100)/20)
        ).aggregate(avg_category_evr=ExpressionWrapper(Avg('evr'), output_field=DecimalField()))

        context['contentcount'] = Evidence.objects.values('content_type').order_by().annotate(
        content_type_count=Count('content_type')).filter(category__slug=self.kwargs['slug'])

        context['researchcount'] = Evidence.objects.values('research_type').order_by().annotate(
        research_type_count=Count('research_type')).filter(category__slug=self.kwargs['slug'])

        return context
#This is the development version of the category view using static data.
def view_category_board(request):
    return render(request, 'category/category_base.html', {
        'evidence_list': [
            {
                'time_elapsed': str(i) + ' hrs ago',
                'tags': ['tag #' + str(n) for n in [1, 2, 3]]
            } for i in [1, 2, 3, 4, 5]
        ],
        'contributors': [
            {'name': 'Jane Doe', 'role': 'practitioner'},
            {'name': 'Miley Jennifer', 'role': 'researcher'},
            {'name': 'Elaine Lwane', 'role': 'chairman'}
        ]
    })
