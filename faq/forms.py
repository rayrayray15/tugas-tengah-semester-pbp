from django import forms
from .models import Qs

class QsForm(forms.ModelForm):
    class Meta:
        model = Qs
        fields = "__all__"

