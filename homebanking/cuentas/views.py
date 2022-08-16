from django.views.generic import TemplateView

class CuentaView(TemplateView):
    template_name = 'cuentas/cuenta.html'
