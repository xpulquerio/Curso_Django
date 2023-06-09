
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(next_page='app_core:home'), name='logout'),
    path('cadastrar/', views.register, name='register'),
    path('resetar-senha/', views.password_reset, name='reset_password'),
    path('confirmar-resetar-senha/<str:key>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar_senha/', views.edit_password, name='edit_password'),
]