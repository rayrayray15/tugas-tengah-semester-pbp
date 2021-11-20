from django import forms
from .models import Comment

# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs= {'rows' : '4'}))

#     class Meta:
#         model = Comment
#         fields = ('content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"