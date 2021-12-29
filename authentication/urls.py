from django.urls import include, path
from .views import login, logoutFlutter, daftar, json_fb

urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),
    path('json_fb', json_fb, name='json_fb'),
]