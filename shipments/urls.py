from django.urls import path
from .views import UpdatePackageStatusView

urlpatterns = [
    path('packages/<str:pk>/status/', UpdatePackageStatusView.as_view(), name='update_package_status'),
]