from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html', {
        'country_evidence': [
            {
                'image': '/static/images/flags/'+country+'.png',
                'title': country.capitalize()
            } for country in ['kenya', 'rwanda', 'egypt', 'south-africa'] * 2
        ]
    })

def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
