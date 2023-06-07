
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
]