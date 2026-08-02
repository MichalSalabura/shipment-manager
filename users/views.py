from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ClientRegistrationForm

# Create your views here.
class RegistrationView(CreateView):
    form_class = ClientRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):

        user = self.request.user
        if user.is_driver:
            return reverse_lazy('driver_dashboard')
        elif user.is_manager:
            return reverse_lazy('manager_dashboard')

        return reverse_lazy('client_dashboard') 