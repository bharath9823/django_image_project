from django import forms
from imgapp.models import imgmodel

class imgform(forms.ModelForm):
    class Meta:
        model = imgmodel
        fields="__all__"