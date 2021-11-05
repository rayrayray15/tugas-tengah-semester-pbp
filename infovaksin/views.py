from django.http import JsonResponse
from django.shortcuts import render
from vaksinfo import settings
import json
import os

# Create your views here.
def index(request):
    return render(request,'infovaksin.html',{})

# def show_json(request):
#     return JsonResponse()

def vaksindata(request) :
    data = [
    {
      "name": "Sinovac",
      "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
      "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
      "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Astrazeneca",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Sinopharm",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Moderna",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Pfizer",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Novavax",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    }
  ]
    return JsonResponse({'datas' : data})