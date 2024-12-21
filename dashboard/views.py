from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import EntradaDeVeiculos


# Página de login
def login_page(request):
    return render(request, 'dashboard/pages/login.html')

# Processamento do login
def do_login(request):
    data = {}
    user = authenticate(username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('home-page')
    else:
        data['message'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger mb-1'
        return render(request, 'dashboard/pages/login.html', context=data)
    
def logouts(request):
    logout(request)
    return redirect('login-page')

# Página inicial
def home(request):
    return render(request,"dashboard/pages/home.html")

# Página de relatórios
def report(request):
    return render(request, "dashboard/pages/relatorio.html")

# Página que exibe o relatório
class ReportList(ListView):
    model = EntradaDeVeiculos
    template_name = 'dashboard/pages/relatorio-exibir.html'

# Página de registro
class RegisterCreate(CreateView):
    model = EntradaDeVeiculos
    fields = [
        'numero_do_registro', 'data_entrada', 'tipo_caminhao', 'placa', 'nome_motorista', 'usuario', 'data_lancamento',
    ]
    template_name = 'dashboard/pages/registro.html'
    success_url = reverse_lazy('register-page')