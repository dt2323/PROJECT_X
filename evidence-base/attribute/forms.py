from django import forms


class AttributeForms(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title of the attribute",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sub_title = forms.CharField(
        max_length=100,
        label='Sub title of the attribute',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    attribute_description = forms.CharField(
        max_length=300,
        required=True,
        label="Describe the attribute",
        widget=forms.Textarea({ 'attrs': 'form-control' })
    )
