from django.urls import include, path
from .views import login, logout


urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logout, name='logoutflutter'),
]