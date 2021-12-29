from django.urls.resolvers import URLPattern
from django.urls import path
from .views import index, addLokasiDef, xml, json

urlpatterns = [
    path('', index, name='lokasi_vaksin'),
    path('tambah-lokasi', addLokasiDef, name = 'lokasi_add'),
    path('xml', xml),
    path('json', json)
]