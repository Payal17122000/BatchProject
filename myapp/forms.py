from django import forms
from django.db import models
from django.db.models import fields
from .models import signup_tbl,notes




class signupForm(forms.ModelForm):
    class Meta:
        model=signup_tbl
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'