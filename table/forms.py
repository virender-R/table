from django import forms
from django.core import validators

def abc(value):
    if not isinstance(value, int):
        raise forms.ValidationError("Only integer values are allowed.")

class FormClass(forms.Form):
    first=forms.CharField(validators=[abc])
    second=forms.CharField()
    