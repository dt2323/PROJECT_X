from django.shortcuts import render
from evidence.models import Evidence, Analysis
from django.views import generic
from category.models import Category

# Create your views here.

#This view lists evidence, filtered by category.
class EvidenceListFiltered(generic.ListView):
    model = Evidence
    select_related = ("category", "user")
    template_name = 'category/view_category.html'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(EvidenceListFiltered, self).get_context_data(**kwargs)
        #context['category'] = Category.objects.all()
        context['category'] = Category.objects.all().filter(slug=self.kwargs['slug'])
        return context
