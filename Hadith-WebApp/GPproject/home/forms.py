from django import forms

class HadithForm(forms.Form):
    search_query = forms.CharField(label='Search in the hadiths', widget=forms.TextInput(attrs={'placeholder': 'Search in the hadiths'}))



