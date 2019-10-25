from django import forms
from .models import UrlRecord


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlRecord
        fields = ["original_url"]
