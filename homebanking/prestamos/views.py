from django.views.generic import TemplateView

# Create your views here.

class PrestamosViews(TemplateView):
    template_name = 'prestamos/prestamos.html'