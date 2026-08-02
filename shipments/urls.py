from django.urls import path
from .views import UpdatePackageStatusView, DriverDashboardView
urlpatterns = [
    path('driver/dashboard/', DriverDashboardView.as_view(), name='driver_dashboard'),
    path('packages/<str:pk>/status/', UpdatePackageStatusView.as_view(), name='update_package_status'),
]