
from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]