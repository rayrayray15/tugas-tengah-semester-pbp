from django import forms
from django.forms import fields, widgets

from .models import Pulau, AddLokasi

class addLokasiForm(forms.ModelForm):
    class Meta:
        model = AddLokasi
        fields = '__all__'
