from django.urls import include, path
from .views import dataPage, index, json_data, logoutUser, dataPage, cekLogin, index_fb, add_fb, fb_list
from .views import loginPage
from .views import daftarPage

urlpatterns = [
    path('', index, name='index'),
    path('feedback', cekLogin, name='feedback'),
    path('add-fb', add_fb, name='add-fb'),
    path('fb-list', fb_list, name='fb-list'),
    path('login', loginPage, name='login'),
    path('daftar', daftarPage, name='daftar'),
    path('logout', logoutUser, name='logout'),
    path('data', dataPage, name='data'),
    path('json',json_data, name='json'),
]