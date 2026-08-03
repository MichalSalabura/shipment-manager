from django import forms
from .models import StatusHistory, Package

class PackageStatusUpdateForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('PICKED_UP', 'Picked Up'),
        ('IN_TRANSIT', 'In Transit'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('DELAYED', 'Delayed'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = StatusHistory
        fields = ['status']

class CreateNewPackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['from_name', 'from_address_line_1', 'from_address_line_2', 'from_address_city',
                  'from_address_post_code', 'from_country', 'to_name', 'to_address_line_1',
                  'to_address_line_2', 'to_address_city', 'to_address_post_code', 'to_country',
                  'recipient_phone', 'recipient_email', 'width', 'height', 'depth']
        widgets = {
            'scheduled_delivery': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'from_address_line_2': forms.TextInput(attrs={'placeholder': 'Apartment, suite, etc. (optional)'}),
            'to_address_line_2': forms.TextInput(attrs={'placeholder': 'Apartment, suite, etc. (optional)'}),
        }

class AssignDriverForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['driver']
        widgets = {
            'driver': forms.Select(attrs={'class': 'form-select'}),
        }