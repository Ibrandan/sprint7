from logging import PlaceHolder
from django.db import models
from cuentas.models import Cliente
from django.forms import ModelForm
from django import forms
from datetime import datetime


PRESTAMOS_CHOICES= [
('personal', 'Prestamo Personal'),
('hipotecario', 'Prestamo Hipotecario'),
('prendario', 'Prestamo Prendario'),
]

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=255)
    loan_date = models.DateField(max_length=9)
    loan_total = models.FloatField()
    customer_id = models.ForeignKey(Cliente, models.CASCADE)

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type','loan_date', 'loan_total']
        labels  = {
            'loan_type':'Tipo del prestamo', 
            'loan_date':'Fecha del Prestamo', 
            'loan_total':'Total', 
        }
        widgets = {
                'loan_type':forms.RadioSelect(choices=PRESTAMOS_CHOICES),
                'loan_date': forms.DateInput(attrs={'value': datetime.now().strftime("%d-%m-%Y"), 'min': datetime.now().strftime("%d-%m-%Y")}),
                'loan_total': forms.NumberInput(attrs={'min': 1, 'value': '1'})
        }