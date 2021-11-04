from django.urls.resolvers import URLPattern
from django.urls import path
from .views import index, addLokasiDef, cuaca

urlpatterns = [
    path('', index, name='lokasi_vaksin'),
    path('tambah-lokasi', addLokasiDef),
    path('weather', cuaca),
]