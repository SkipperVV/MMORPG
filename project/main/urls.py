from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView, name='home'),
    path('about/', views.AboutView, name='about'),
]