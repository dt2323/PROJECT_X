from django import forms

from evidence import models
from . models import Evidence, Analysis


class EvidenceForm(forms.ModelForm):
    class Meta:
        fields = ('title','contributors_note','website','publisher','publication_date','content_type','research_type','category')
        model = models.Evidence

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["category"].queryset = (
                models.Category.objects.filter(
                    pk__in=user.category.values_list("catgeory__pk")#Will need to change to not just user category but attribute category's
                )
            )


#class AnalysisForm(forms.ModelForm):

#    class Meta:
#        model = models.Analysis
#        fields = ('title', 'content_rating_1', 'content_rating_1_comment', 'content_rating_2', 'content_rating_2_comment',
#        'content_rating_3', 'content_rating_3_comment','content_rating_4', 'content_rating_4_comment','content_rating_5', 'content_rating_5_comment',
#        'source_rating_1', 'source_rating_1_comment','source_rating_2', 'source_rating_2_comment',
#        'source_rating_3', 'source_rating_3_comment','source_rating_4', 'source_rating_4_comment','source_rating_5', 'source_rating_5_comment')
