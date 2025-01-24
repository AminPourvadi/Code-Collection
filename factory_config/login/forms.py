from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="ایمیل", max_length=255)
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
