from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone_number")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.CLIENT
        if commit:
            user.save()
        return user