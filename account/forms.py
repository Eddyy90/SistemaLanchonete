from dataclasses import fields
from django import forms
from .models import *

class CadForm(forms.ModelForm):
    class Meta:
        model = CadUser
        fields = ["nome", "email", "senha"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = LogUser
        fields = ["email", "senha"]