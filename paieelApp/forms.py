from django.db import models
from django import forms

class IngresoForm(forms.Form):
    foto = forms.FileField()

    def __str__(self):
        return self.foto