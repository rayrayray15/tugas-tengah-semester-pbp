from django import forms
from .models import Feedback2

class FeedbackForm2(forms.ModelForm):
    class Meta:
        model = Feedback2
        fields = "__all__"