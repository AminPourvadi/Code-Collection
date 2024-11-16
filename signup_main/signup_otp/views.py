# from django.shortcuts import render
# # ویو ثبت نام
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import CustomUser  
# from .forms import RegistrationForm  
# import random 

# def generate_otp():
#     return random.randint(100000, 999999)

# def signup_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save() 
#             otp = generate_otp()
#             # request.session['otp'] = otp  # ذخیره کد OTP در سشن برای استفاده در صورت نیاز
#             return HttpResponse(f"کد OTP شما: {otp}")
#             # print(f"کد OTP برای شماره {otp}")
#             # request.session['otp'] = otp  
#             # request.session['user_id'] = user.id 

#             # return  HttpResponse(f"داده دریافت شده: {otp}")
#         else:
#             return HttpResponse("opssss")

#     else:
#         form = RegistrationForm()
    
#         return render(request, 'signup_otp/signup.html', {'form': form})

# کد جدید----------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser  
from .forms import RegistrationForm  
import random
from rest_framework.views import APIView
from .serializers import OTPSerializer
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import OTP
import random
import string

class VerifyOTPView(APIView):
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')

        try:
            otp = OTP.objects.get(phone_number=phone_number, otp_code=otp_code)
        except OTP.DoesNotExist:
            return Response({"error": "OTP نامعتبر است."}, status=400)

        if otp.is_expired():
            return Response({"error": "کد تایید منقضی شده است."}, status=400)

        otp.is_verified = True
        otp.save()

        user = otp.user
        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })


@api_view(['POST'])
def send_otp(request):
    serializer = OTPSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            otp_code = ''.join(random.choices(string.digits, k=6))  
            otp = OTP.objects.create(user=user, code=otp_code)

@api_view(['POST'])
def verify_otp(request):
    otp_code = request.data.get('otp_code')
    phone_number = request.data.get('phone_number')

    if not otp_code or not phone_number:
        return Response({'error': 'OTP code and phone_number are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(phone_number=phone_number).first()
    if user:
        otp = OTP.objects.filter(user=user, otp_code=otp_code, is_verified=False).first()

        if otp:
            if otp.is_expired():
                return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            
            otp.is_verified = True
            otp.save()
            return Response({'message': 'OTP verified successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

def generate_otp():
    return random.randint(100000, 999999)

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['phone_number']
            if CustomUser.objects.filter(username=username).exists():
                return HttpResponse("این نام کاربری قبلاً ثبت شده است.")
            user=form.save(commit=False)   
            otp = generate_otp()
            request.session['otp'] = otp
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return HttpResponse(f"کد شما فرستاده شده")

        else:
            return HttpResponse("فرم معتبر نیست.")

    else:
        form = RegistrationForm()
    
    return render(request, 'signup_otp/signup.html', {'form': form})
