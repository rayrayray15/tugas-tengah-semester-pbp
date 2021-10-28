from django.urls import include, path
from .views import dataPage, index, json_data, logoutUser, dataPage
from .views import loginPage
from .views import daftarPage

urlpatterns = [
    path('', index, name='index'),
    path('login', loginPage, name='login'),
    path('daftar', daftarPage, name='daftar'),
    path('logout', logoutUser, name='logout'),
    path('data', dataPage, name='data'),
    path('json',json_data, name='json'),
]