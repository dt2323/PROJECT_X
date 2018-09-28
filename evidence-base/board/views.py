from __future__ import unicode_literals
from . import forms
from category.forms import CategoryForms
from django.shortcuts import render


def add_board(request):
    form = forms.BoardForm()
    return render(request, 'board/add_board.html', { 'board_form': form, 'category_form': CategoryForms })


def view_board(request):
    return render(request, 'board/view_board.html', {
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
