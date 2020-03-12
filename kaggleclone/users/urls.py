# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('api/v1/', views.UserListView.as_view()),
]
