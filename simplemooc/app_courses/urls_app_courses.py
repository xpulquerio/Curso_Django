
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    #path('<int:pk>/', views.details, name='details') #Jeito novo
    #url(r'^(?P<pk>\d)/$', 'details', name='details') #Jeito antigo
    path('<slug>/', views.details, name='details') #Jeito novo usando Slug ao invés do id
    #url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),#Jeito antigo usando Slug ao invés do id
]

