from django.urls import include, path
from .views import index, index_mview

urlpatterns = [
    path('', index, name='index_stats'),
    path('mobile-view/', index_mview, name='index_stats_mview'),
]