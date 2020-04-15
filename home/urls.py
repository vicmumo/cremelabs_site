from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('r^$', views.home),
    path('', views.home),
]