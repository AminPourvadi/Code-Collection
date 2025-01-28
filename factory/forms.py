from django import forms
from .models import TranslatedText

class TranslatedTextForm(forms.ModelForm):
    class Meta:
        model = TranslatedText
        fields = ['original_text', 'translated_en', 'translated_ar']
        widgets = {
            'original_text': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
            'translated_en': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
            'translated_ar': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
        }

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'ایمیل'
    }))

    password = forms.CharField(label="گذرواژه", widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'گذرواژه'
    }))

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']

    name = forms.CharField(label="نام", widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'نام'
    }))
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'ایمیل'
    }))
    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'گذرواژه'
    }))
    password2 = forms.CharField(label="تکرار گذرواژه", widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'تکرار گذرواژه'
    }))
