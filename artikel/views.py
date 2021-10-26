from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artikel

def index(request):
    return render(request, 'index.html', {}) 

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel_list.html'
    ordering = ['-id']

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel_detail.html'