from django.urls import path

from dashboard import views

urlpatterns = [
    path('login', views.login_page, name='login-page'),
    path('do-login', views.do_login, name='do-login'),
    path('logout', views.logouts, name='log-out'),
    path('', views.home, name='home-page'),
    path('relatorio/', views.report, name='report-page'),
    path('relatorio/lista-de-veiculos-a-expedir', views.ReportList.as_view(), name='list-report-page'),
    path('registro/', views.RegisterCreate.as_view(), name='register-page'),
]