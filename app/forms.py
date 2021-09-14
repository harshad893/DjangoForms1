from django import forms
from django.core import validators

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()