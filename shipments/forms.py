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