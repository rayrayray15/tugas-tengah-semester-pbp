from django.urls import path
from .views import index, qs

urlpatterns = [
    path('', index, name='index_faq'),
    path('qs', qs, name='qs'),

]
