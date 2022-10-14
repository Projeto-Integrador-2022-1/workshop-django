from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
]