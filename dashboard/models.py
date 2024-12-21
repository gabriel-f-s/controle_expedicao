from datetime import datetime

from django.db import models

# Create your models here.

TRUCK_CHOICES = (
    ("Carreta Bau","Carreta - Baú"),
    ("Carreta Sider", "Carreta - Sider"),
    ("Truck Bau", "Truck - Baú"),
    ("Truck Sider", "Truck - Sider"),
)

class EntradaDeVeiculos(models.Model):
    numero_do_registro = models.IntegerField(verbose_name="Número do Registro")
    data_entrada = models.DateTimeField(default=datetime.now, verbose_name="Data de Entrada")
    tipo_caminhao = models.CharField(max_length=20, choices=TRUCK_CHOICES, verbose_name="Tipo de Caminhão")
    placa = models.CharField(max_length=7, verbose_name="Placa do Veículo")
    nome_motorista = models.CharField(max_length=50, verbose_name="Nome do Motorista")
    usuario = models.CharField(max_length=50, verbose_name="Usuário")
    data_lancamento = models.DateTimeField(default=datetime.now, verbose_name="Data de Lançamento", blank=True)
    expedido = models.BooleanField(default=False, blank=True)