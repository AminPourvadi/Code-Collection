from django.shortcuts import render, redirect
from register.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # مسیر ورود کاربر
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})
