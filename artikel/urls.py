from django.urls import path
from .views import ArtikelListView, ArtikelDetailView, AddArticleView, get_object, AddArticleFlutter

urlpatterns = [
    path('', ArtikelListView.as_view(), name='artikel_list'),
    path('json', get_object, name='json'),
    path('article_flutter', AddArticleFlutter, name='article_flutter'),
    path('add-article', AddArticleView.as_view(), name = "article_cbv"),
    path('<slug:slug>', ArtikelDetailView.as_view(), name='artikel_detail'),
]