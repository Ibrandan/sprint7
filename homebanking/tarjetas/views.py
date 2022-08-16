from django.views.generic import TemplateView

# Create your views here.

class TarjetasView(TemplateView):
    template_name = 'Tarjetas/tarjetas.html'
