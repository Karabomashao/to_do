from django import forms
from .models import tasklist

class Taskform(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = [
            "user_auth",
            "title",
            "description",
            "complete",
        ]

class RawProductForm(forms.Form):
    user_auth = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()
    complete = forms.BooleanField()

