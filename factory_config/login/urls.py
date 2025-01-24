from django.urls import path
from .views import user_login , api_login

urlpatterns = [
    path('form/', user_login, name='login'),
    path('api/', api_login, name='api_login'),
]
