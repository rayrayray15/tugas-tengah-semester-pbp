from django.urls import include, path
from .views import login, logoutFlutter, daftar, fb_json

urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),
    path('feedbackjson', fb_json, name='fb_json'),
]