from django import forms

# creating a form


class InputForm(forms.Form):

    motivo = forms.CharField()
    monto = forms.FloatField()
    destinatario = forms.CharField()
