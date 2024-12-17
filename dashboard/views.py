from django.shortcuts import render


def home(request):
    return render(request,"dashboard/pages/home.html")

def relatorio(request):
    return render(request, "dashboard/pages/relatorio.html")


def registro(request):
    return render(request, "dashboard/pages/registro.html")