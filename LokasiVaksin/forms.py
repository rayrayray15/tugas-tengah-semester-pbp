from django import forms
from django.forms import fields, widgets

from .models import Pulau, AddLokasi, Provinsi

class addLokasiForm(forms.ModelForm):
    class Meta:
        model = AddLokasi
        fields = '__all__'

    # # def __init__(self, *args, **kwargs):
    # #     super().__init__(*args, **kwargs)
    # #     self.fields['provinsi'].queryset = Provinsi.objects.none()

    # #     if 'pulau' in self.data:
    # #         try:
    # #             pulau_id = int(self.data.get('pulau'))
    # #             self.fields['provinsi'].queryset = Provinsi.objects.filter(pulau_id = pulau_id).order_by('NamaLokasi')
    # #         except(ValueError, TypeError):
    # #             pass
    # #     elif self.instance.pk:
    # #         self.fields['provinsi'].queryset = self.instance.Pulau.Provinsi_set.order_by('NamaLokasi')
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['provinsi'].queryset = Provinsi.objects.none()

    #     if 'pulau' in self.data:
    #         try:
    #             pulau_id = int(self.data.get('pulau'))
    #             self.fields['provinsi'].queryset = Provinsi.objects.filter(pulau_id=pulau_id).order_by('NamaLokasi')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['provinsi'].queryset = self.instance.Pulau.Provinsi_set.order_by('NamaLokasi')
