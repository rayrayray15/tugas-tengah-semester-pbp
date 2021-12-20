from django.urls import path
from .views import ArtikelListView, ArtikelDetailView, AddArticleView, json

urlpatterns = [
    path('', ArtikelListView.as_view(), name='artikel_list'),
    path('json', json, name='json'),
    path('add-article', AddArticleView.as_view(), name = "article_cbv"),
    path('<slug:slug>', ArtikelDetailView.as_view(), name='artikel_detail'),
]