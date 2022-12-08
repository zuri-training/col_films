from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_videos/', VideoCreateView.as_view()),
    path('all_users/', AllUsers.as_view()),
]