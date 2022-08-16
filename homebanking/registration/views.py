from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import CustomRegistrationForm


class SignUp(generic.CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return HttpResponseRedirect(reverse('cuentas:cuenta'))