from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Artikel

def index(request):
    return render(request, 'index.html', {}) 

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel_list.html'
    ordering = ['-id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(body__icontains=query) | Q(title__icontains=query))
        else:
            object_list = self.model.objects.all()
        return object_list

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel_detail.html'

def get_article_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        articles = Artikel.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains = q)
        ).distinct()

        for article in articles:
            queryset.append(article);
    return list(set(queryset))