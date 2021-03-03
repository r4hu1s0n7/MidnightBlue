from django import forms
from django.db.models import fields
from MidnightBlue.models import *

class MovieDBForm(forms.ModelForm):
    class Meta:
        model = MovieDB
        fields = "__all__"