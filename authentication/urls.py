from django.urls import include, path
from .views import login, logoutFlutter, daftar


urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),
]