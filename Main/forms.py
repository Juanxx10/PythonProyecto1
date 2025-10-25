from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Avatar

class EditUserForm(UserChangeForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        required=True,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']