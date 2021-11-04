from .models import Artikel
from django import forms

class ArtikelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArtikelForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for article in self.fields.keys():
            self.fields[article].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Artikel
        fields = "__all__" 