from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from .models import Artikel
from .forms import ArtikelForm
import json

def get_object(request):
    data = [artikel.json() for artikel in Artikel.objects.all().order_by('-id')]
    return HttpResponse(json.dumps(data), content_type="application/json")

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel_list.html'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            object_list = self.model.objects.filter(Q(body__icontains=query) | Q(title__icontains=query)).order_by('-id')
        else:
            object_list = self.model.objects.all().order_by('-id')
        return object_list

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtikelDetailView , self).get_context_data(**kwargs)
        context['articles'] = Artikel.objects.order_by('-id')[:10]
        return context

class AddArticleView(View):
    form_class = ArtikelForm
    template_name = "add_article.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        articles = Artikel.objects.all().order_by('-id')
        return render(self.request, self.template_name, 
            {"form": form, "articles": articles})

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)

        return JsonResponse({"error": ""}, status=400)