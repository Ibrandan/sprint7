from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CuentaView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/cuenta.html'

class ActividadView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/actividad.html'

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/perfil.html'

class FondosView(LoginRequiredMixin, TemplateView):
    template_name = 'cuentas/fondos.html'



