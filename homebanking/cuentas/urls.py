from django.urls import path

from . import views

app_name = 'cuentas'
urlpatterns = [
    path('', views.cuenta, name='cuenta'),
]