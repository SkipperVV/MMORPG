from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('out', views.logoutView, name='logout'),
]