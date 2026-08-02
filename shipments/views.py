from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Package, StatusHistory
from .forms import PackageStatusUpdateForm
# Create your views here.

class UpdatePackageStatusView(LoginRequiredMixin, CreateView):
    model = StatusHistory
    form_class = PackageStatusUpdateForm
    template_name = 'shipments/update_status.html'
    success_url = reverse_lazy('driver_dashboard')

    def form_valid(self, form):
        form.instance.package = get_object_or_404(Package, pk = self.kwargs['pk'])
        form.instance.logged_by = self.request.user
        return super().form_valid(form)

class DriverDashboardView(LoginRequiredMixin, ListView):
    model = Package
    template_name = "shipments/driver_dashboard.html"
    context_object_name = "assigned_packages"

    def get_queryset(self):
        if hasattr(self.request.user, 'driver_profile'):
            return Package.objects.filter(driver=self.request.user.driver_profile)
        return Package.objects.none()
