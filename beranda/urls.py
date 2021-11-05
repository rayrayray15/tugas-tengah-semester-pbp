from django.urls import include, path
from .views import dataPage, index, json_data, logoutUser, dataPage, feedback
from .views import loginPage
from .views import daftarPage

urlpatterns = [
    path('', index, name='index'),
    path('feedback', feedback, name='feedback'),
    path('login', loginPage, name='login'),
    path('daftar', daftarPage, name='daftar'),
    path('logout', logoutUser, name='logout'),
    path('data', dataPage, name='data'),
    path('json',json_data, name='json'),
]