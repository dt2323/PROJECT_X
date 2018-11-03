from django import forms
from board import models
from board.models import Board
from board.widgets import RangeInput


class BoardForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'sub_title', 'board_description',
        'content_rating_1_title', 'content_rating_1_weight',
        'content_rating_2_title', 'content_rating_2_weight',
        'content_rating_3_title', 'content_rating_3_weight',
        'content_rating_4_title', 'content_rating_4_weight',
        'content_rating_5_title', 'content_rating_5_weight',
        'source_rating_1_title', 'source_rating_1_weight',
        'source_rating_2_title', 'source_rating_2_weight',
        'source_rating_3_title', 'source_rating_3_weight',
        'source_rating_4_title', 'source_rating_4_weight',
        'source_rating_5_title', 'source_rating_5_weight')
        model = models.Board

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Give your new evidence board a name (required)'}),
        'sub_title':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Provide a one line description of your evidence board (optional)'}),
        'board_description':forms.Textarea(attrs={'class':'form-control',
        'placeholder':'Provide a description of what this evidence board is about (required)'}),

        'content_rating_1_title':forms.TextInput(attrs={'class':'form-control'}),
        'content_rating_1_weight':RangeInput(),

        'content_rating_2_title':forms.TextInput(attrs={'class':'form-control'}),
        'content_rating_2_weight':RangeInput(),

        'content_rating_3_title':forms.TextInput(attrs={'class':'form-control'}),
        'content_rating_3_weight':RangeInput(),

        'content_rating_4_title':forms.TextInput(attrs={'class':'form-control'}),
        'content_rating_4_weight':RangeInput(),

        'content_rating_5_title':forms.TextInput(attrs={'class':'form-control'}),
        'content_rating_5_weight':RangeInput(),

        'source_rating_1_title':forms.TextInput(attrs={'class':'form-control'}),
        'source_rating_1_weight':RangeInput(),

        'source_rating_2_title':forms.TextInput(attrs={'class':'form-control'}),
        'source_rating_2_weight':RangeInput(),

        'source_rating_3_title':forms.TextInput(attrs={'class':'form-control'}),
        'source_rating_3_weight':RangeInput(),

        'source_rating_4_title':forms.TextInput(attrs={'class':'form-control'}),
        'source_rating_4_weight':RangeInput(),

        'source_rating_5_title':forms.TextInput(attrs={'class':'form-control'}),
        'source_rating_5_weight':RangeInput(),

        }

#    title = forms.CharField(
#        label='Board Title',
#        required=True,
#        error_messages={'required': 'Please give your board a title'})
#    sub_title = forms.CharField(
#        label='Sub-title',
#        widget=forms.TextInput(attrs={'class': 'form-control'}) )
#    board_description = forms.CharField(
#        required=True,
#        label='Board Description',
#        widget=forms.Textarea(attrs={'class': 'form-control'}),
#        error_messages={'required': 'Please enter a description for your board'}    )
