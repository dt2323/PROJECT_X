from django import forms

from evidence import models
from . models import Evidence, Analysis
from evidence.widgets import RangeInput


class EvidenceForm(forms.ModelForm):
    class Meta:
        fields = ('title','contributors_note','website','publisher',
        'publication_date','content_type','research_type','category')
        model = models.Evidence

        widgets = {'title':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'The title of your evidence'}),
        'contributors_note':forms.Textarea(attrs={'class':'form-control',
        'placeholder':'Explain why you are adding the evidence to this category'}),
        'website':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Copy & paste a link to the evidence so others can find it'}),
        'publisher':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'The author/organisation that created the evidence'}),
        'content_type':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'What kind of content is this? e.g. Opinion, analysis, reporting etc.'}),
        'research_type':forms.TextInput(attrs={'class':'form-control',
        'placeholder':'What kind of research is this based on? e.g. Quantitative analysis, qualitative research. Add as many tags as you like, seperated by commas'})

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["category"].queryset = (
                models.Category.objects.filter(
                    pk__in=user.category.values_list("catgeory__pk")#Will need to change to not just user category but attribute category's
                )
            )


class AnalysisForm(forms.ModelForm):

    class Meta:
        model = models.Analysis
        fields = ('title', 'key_finding1', 'key_finding2', 'key_finding3', 'content_rating_1', 'content_rating_1_comment', 'content_rating_2', 'content_rating_2_comment',
        'content_rating_3', 'content_rating_3_comment','content_rating_4', 'content_rating_4_comment','content_rating_5', 'content_rating_5_comment',
        'source_rating_1', 'source_rating_1_comment','source_rating_2', 'source_rating_2_comment',
        'source_rating_3', 'source_rating_3_comment','source_rating_4', 'source_rating_4_comment','source_rating_5', 'source_rating_5_comment')

        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'key_finding1':forms.Textarea(attrs={'class':'form-control'}),
        'key_finding2':forms.Textarea(attrs={'class':'form-control'}),
        'key_finding3':forms.Textarea(attrs={'class':'form-control'}),
        'content_rating_1':RangeInput(),
        'content_rating_1_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'content_rating_2':RangeInput(),
        'content_rating_2_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'content_rating_3':RangeInput(),
        'content_rating_3_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'content_rating_4':RangeInput(),
        'content_rating_4_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'content_rating_5':RangeInput(),
        'content_rating_5_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),

        'source_rating_1':RangeInput(),
        'source_rating_1_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'source_rating_2':RangeInput(),
        'source_rating_2_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'source_rating_3':RangeInput(),
        'source_rating_3_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'source_rating_4':RangeInput(),
        'source_rating_4_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),
        'source_rating_5':RangeInput(),
        'source_rating_5_comment':forms.Textarea(attrs={'class':'form-control', 'size': '5'}),

        }
