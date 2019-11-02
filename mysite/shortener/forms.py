from django import forms
from .models import UrlRecord


class UrlForm(forms.ModelForm):
    original_url = forms.URLField(widget=forms.TextInput(attrs={"class": "form-control"})) 
    class Meta:
        model = UrlRecord
        fields = ["original_url"]
