from datetime import date, datetime
from math import frexp
from sqlite3 import IntegrityError
from unicodedata import name
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.shortcuts import render
from .forms import InputForm

from cuentas.models import Cliente


def CuentaView(request):
    username = Cliente.objects.all().filter(customer_username=request.user).first()

    transactions = Movimientos.objects.all().filter(
        account_number=username.customer_id).order_by('-date')[:7]
    for texto in Cuenta.objects.all():
        if texto.customer_id == username.customer_id:
            print('yay')
    cash = Cuenta.objects.filter(customer_id=username.customer_id).first()

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
            username = Cliente.objects.all().filter(customer_username=request.user).first()
            cash = Cuenta.objects.filter(
                customer_id=username.customer_id).first().balance

            try:
                dest = Cliente.objects.all().filter(
                    customer_id=int(destinatario)).first()
                print(cash, monto, float(cash) > float(monto), username, dest)
                if float(cash) > float(monto) and float(monto) > 0:
                    print("asds")
                    if username != dest:
                        print("asds")
                        out = Movimientos(account_number=dest, amount=monto, reason=motivo,
                                          status="Recibido", date=datetime.now(), operation_type="Transferencia")
                        inp = Movimientos(account_number=username, amount=monto, reason=motivo,
                                          status="Enviado", date=datetime.now(), operation_type="Transferencia")
                        out.save()
                        inp.save()
                        sender = Cuenta.objects.filter(
                            customer_id=username.customer_id).first()
                        sender.balance -= monto
                        reciever = Cuenta.objects.filter(
                            customer_id=dest).first()
                        reciever.balance += monto
                        sender.save()
                        reciever.save()

                    else:
                        context['error'] = 'No podes transferirte a vos mismo'
                        print('err')

                else:
                    print("as")
                    context['error'] = 'No tenes saldo suficiente'
            except IntegrityError:
                context['error'] = f'No existe el usuario {destinatario}'

    return render(request, "cuentas/transferencias.html", context)


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/perfil.html'


class FondosView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/fondos.html'
