from django.urls import path
from . import views
from .views import signup_view

urlpatterns = [
    path('signup_with_otp/', signup_view, name='signup'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]