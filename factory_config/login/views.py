from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('register')  # تغییر مسیر به صفحه اصلی یا هر صفحه دیگر
            else:
                return render(request, 'login/login.html', {'form': form, 'error': 'اطلاعات ورود نادرست است.'})
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


@api_view(['POST'])
def api_login(request):
    if request.method == 'POST':
        try:
            # دریافت داده‌های JSON از درخواست
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # انجام لاگین (مثال ساده)
            if email == "testuser@example.com" and password == "password123":
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"error": "Invalid email or password"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)