from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/<int:id>/', views.dashboard, name = 'dashboard' )
]