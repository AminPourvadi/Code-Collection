from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser

# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100, label='نام')
#     phone_number = forms.CharField(max_length=15, label='شماره تلفن')
#     # otp = forms.CharField(max_length=6, label='کد OTP', required=False)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number'] 
