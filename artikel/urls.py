from django.urls import path
from .views import ArtikelListView, ArtikelDetailView

urlpatterns = [
    path('', ArtikelListView.as_view(), name='artikel_list'),
    path('<slug:slug>', ArtikelDetailView.as_view(), name='artikel_detail')
]