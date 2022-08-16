from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/cuenta.html'
