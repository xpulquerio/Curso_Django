
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastrar/', views.register, name='register'),

]