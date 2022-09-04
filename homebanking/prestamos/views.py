from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import PrestamoForm

class PrestamosViews(LoginRequiredMixin, TemplateView):
    template_name = 'prestamos/prestamos.html'

class PrestamosForm(generic.CreateView):
    form_class = PrestamoForm
    success_url = reverse_lazy('prestamos:prestamos')
    template_name = 'prestamos/prestamos.html'

