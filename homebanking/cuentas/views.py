from datetime import date, datetime
from math import frexp
from sqlite3 import IntegrityError
from unicodedata import name
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.shortcuts import render
from .forms import InputForm


def CuentaView(request):
    username = Cliente.objects.all().filter(customer_username=request.user).first()

    transactions = Movimientos.objects.all().filter(
        account_number=username.customer_id).order_by('-date')
    cash = Cuenta.objects.filter(account_id=username.customer_id).first()

    return render(request, 'cuentas/cuenta.html',
                  {'transactions': transactions, 'cash': cash})


""" class CuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/cuenta.html' """


def ActividadView(request):
    username = Cliente.objects.all().filter(customer_username=request.user).first()

    transactions = Movimientos.objects.all().order_by('-date').filter(
        account_number=username.customer_id)

    return render(request, 'cuentas/actividad.html',
                  {'transactions': transactions})


def TransferenciaView(request):
    context = {}
    context['form'] = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            monto = form.cleaned_data['monto']
            motivo = form.cleaned_data['motivo']
            destinatario = form.cleaned_data['destinatario']
            try:
                dest = Cliente.objects.all().filter(
                    customer_id=int(destinatario)).first()
                p = Movimientos(account_number=dest, amount=monto, reason=motivo,
                                status="ACEPTADO", date=datetime.now(), operation_type="Transferencia")
                p.save()
            except IntegrityError:
                context['error'] = f'No existe el usuario {destinatario}'

    return render(request, "cuentas/transferir.html", context)


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/perfil.html'


class FondosView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/fondos.html'
