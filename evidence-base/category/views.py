from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from evidence.models import Evidence, Analysis
from django.views import generic
from django.db.models import Count, Avg, IntegerField, F
from django.utils.timesince import timesince

from category.models import Category


# This view lists evidence, filtered by category.
class EvidenceListFiltered(generic.ListView):
    model = Evidence
    select_related = ("category", "user")
    template_name = 'category/view_category.html'

    def get_queryset(self):
        qs = Evidence.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug']).annotate(
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
                suwr=(F('category__attribute__board__content_rating_1_weight') * F('cr1_avg')) +
                     (F('category__attribute__board__content_rating_2_weight') * F('cr2_avg')) +
                     (F('category__attribute__board__content_rating_3_weight') * F('cr3_avg')) +
                     (F('category__attribute__board__content_rating_4_weight') * F('cr4_avg')) +
                     (F('category__attribute__board__content_rating_5_weight') * F('cr5_avg')) +
                     (F('category__attribute__board__source_rating_1_weight') * F('sr1_avg')) +
                     (F('category__attribute__board__source_rating_2_weight') * F('sr2_avg')) +
                     (F('category__attribute__board__source_rating_3_weight') * F('sr3_avg')) +
                     (F('category__attribute__board__source_rating_4_weight') * F('sr4_avg')) +
                     (F('category__attribute__board__source_rating_5_weight') * F('sr5_avg'))
            ).annotate(
                smvc=(F('category__attribute__board__content_rating_1_weight') * 5) +
                     (F('category__attribute__board__content_rating_2_weight') * 5) +
                     (F('category__attribute__board__content_rating_3_weight') * 5) +
                     (F('category__attribute__board__content_rating_4_weight') * 5) +
                     (F('category__attribute__board__content_rating_5_weight') * 5) +
                     (F('category__attribute__board__source_rating_1_weight') * 5) +
                     (F('category__attribute__board__source_rating_2_weight') * 5) +
                     (F('category__attribute__board__source_rating_3_weight') * 5) +
                     (F('category__attribute__board__source_rating_4_weight') * 5) +
                     (F('category__attribute__board__source_rating_5_weight') * 5)
            ).annotate(
                evr=(
                        ((F('suwr') / F('smvc')) * 100) / 20))

        return qs

    def get_context_data(self, **kwargs):
        context = super(EvidenceListFiltered, self).get_context_data(**kwargs)
        context['category'] = Category.objects.filter(slug=self.kwargs['slug'])

        context['evidence_stats'] = Evidence.objects.filter(category__slug=self.kwargs['slug']).annotate(
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
            suwr=(F('category__attribute__board__content_rating_1_weight') * F('cr1_avg')) +
                 (F('category__attribute__board__content_rating_2_weight') * F('cr2_avg')) +
                 (F('category__attribute__board__content_rating_3_weight') * F('cr3_avg')) +
                 (F('category__attribute__board__content_rating_4_weight') * F('cr4_avg')) +
                 (F('category__attribute__board__content_rating_5_weight') * F('cr5_avg')) +
                 (F('category__attribute__board__source_rating_1_weight') * F('sr1_avg')) +
                 (F('category__attribute__board__source_rating_2_weight') * F('sr2_avg')) +
                 (F('category__attribute__board__source_rating_3_weight') * F('sr3_avg')) +
                 (F('category__attribute__board__source_rating_4_weight') * F('sr4_avg')) +
                 (F('category__attribute__board__source_rating_5_weight') * F('sr5_avg'))
        ).annotate(
            smvc=(F('category__attribute__board__content_rating_1_weight') * 5) +
                 (F('category__attribute__board__content_rating_2_weight') * 5) +
                 (F('category__attribute__board__content_rating_3_weight') * 5) +
                 (F('category__attribute__board__content_rating_4_weight') * 5) +
                 (F('category__attribute__board__content_rating_5_weight') * 5) +
                 (F('category__attribute__board__source_rating_1_weight') * 5) +
                 (F('category__attribute__board__source_rating_2_weight') * 5) +
                 (F('category__attribute__board__source_rating_3_weight') * 5) +
                 (F('category__attribute__board__source_rating_4_weight') * 5) +
                 (F('category__attribute__board__source_rating_5_weight') * 5)
        ).annotate(
            evr=(
                    ((F('suwr') / F('smvc')) * 100) / 20)).aggregate(
            avg_category_evr=Avg('evr'))

        context['contentcount'] = Evidence.objects.values('content_type').order_by().annotate(
            content_type_count=Count('content_type')).filter(category__slug=self.kwargs['slug'])

        context['researchcount'] = Evidence.objects.values('research_type').order_by().annotate(
            research_type_count=Count('research_type')).filter(category__slug=self.kwargs['slug'])

        return context


# This is the development version of the category view using static data.
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
