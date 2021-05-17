from django import forms


class SearchForm(forms.Form):
    search_key = forms.CharField(max_length=100)