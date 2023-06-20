"""
URL configuration for simplemooc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf import settings #Pegar todas as settings para lidar com as imagens carregadas pelo painel
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('app_core.urls_app_core', 'app_core'), namespace='app_core')),
    path('cursos/', include(('app_courses.urls_app_courses', 'app_courses'), namespace='app_courses')),    
    path('admin/', admin.site.urls),
    path('conta/', include(('app_accounts.urls_app_accounts','app_accounts'), namespace='app_accounts'))
]

if settings.DEBUG: #Se estiver no ambiente de Debug vou adicionar uma linha a mais na PATTERNS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)