from django.urls import include, path
from .views import login, logoutFlutter, daftar, json_fb, fb_json, feedback_json, ListFeedback, DetailFeedback

urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),
    # path('json_fb', feedback_json, name='json_fb'),
    path('json_fb', ListFeedback.as_view()),
    path('<int:pk>/', DetailFeedback.as_view())
]