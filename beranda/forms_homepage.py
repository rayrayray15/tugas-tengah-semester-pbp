from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import fields

class FeedbackForm(forms.Form) :
    CHOICES = [('B', 'Bad'), ('A', 'Average'), ('G', 'Good')]
    experience = forms.CharField(label='experience', widget=forms.RadioSelect(choices=CHOICES))
    comments = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100)
    email = forms.CharField()

