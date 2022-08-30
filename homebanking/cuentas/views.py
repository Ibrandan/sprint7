from math import frexp
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.shortcuts import render

def CuentaView(request):
    username = Cliente.objects.all().filter(customer_username = request.user).first()

    transactions = Movimientos.objects.all().filter(account_number = username.customer_id)
    cash = Cuenta.objects.filter(account_id = username.customer_id ).first()
    
    return render(request,'cuentas/cuenta.html',
    {'transactions':transactions,'cash':cash})


""" class CuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/cuenta.html' """

class ActividadView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/actividad.html'

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/perfil.html'

class FondosView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/fondos.html'



