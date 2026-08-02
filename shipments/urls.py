from django.urls import path
from .views import UpdatePackageStatusView, DriverDashboardView, ClientDashboardView
urlpatterns = [
    path('driver/dashboard/', DriverDashboardView.as_view(), name='driver_dashboard'),
    path('packages/<str:pk>/status/', UpdatePackageStatusView.as_view(), name='update_package_status'),
    path('client/dashboard/', ClientDashboardView.as_view(), name='client_dashboard'),
]