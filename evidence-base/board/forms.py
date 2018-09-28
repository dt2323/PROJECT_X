from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        label='Title of the board',
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter the board title'},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sub_title = forms.CharField(
        label='Sub-title the board',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    board_description = forms.CharField(
        max_length=300,
        required=True,
        label="Describe the board",
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        error_messages={'required': 'Please enter board description'}
    )


class WeightsForm(forms.Form):
    content_rating_1_title = forms.CharField(
        max_length=50,
        label="Content Characterstic 1",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content_rating_1_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type':'range', 'step': '1'})
    )

    content_rating_2_title = forms.CharField(
        max_length=50,
        label="Content Characterstic 2",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content_rating_2_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    content_rating_3_title = forms.CharField(
        max_length=50,
        label="Content Characterstic 3",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content_rating_3_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    content_rating_4_title = forms.CharField(
        max_length=50,
        label="Content Characterstic 4",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content_rating_4_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    content_rating_5_title = forms.CharField(
        max_length=50,
        label="Content Characterstic 5",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content_rating_5_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    source_rating_1_title = forms.CharField(
        max_length=50,
        label="Source Characterstic 1",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    source_rating_1_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    source_rating_2_title = forms.CharField(
        max_length=50,
        label="Source Characterstic 2",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    source_rating_2_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    source_rating_3_title = forms.CharField(
        max_length=50,
        label="Source Characterstic 3",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    source_rating_3_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    source_rating_4_title = forms.CharField(
        max_length=50,
        label="Source Characterstic 4",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    source_rating_4_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )

    source_rating_5_title = forms.CharField(
        max_length=50,
        label="Source Characterstic 5",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    source_rating_5_weight = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'type': 'range', 'step': '1'})
    )
