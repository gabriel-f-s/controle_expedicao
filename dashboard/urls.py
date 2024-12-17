from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('/relatorio', views.relatorio, name='relatory-page'),
    path('/registro', views.registro, name='register-page'),
]