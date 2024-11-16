from django.db import models

# Create your models here.
# مدل ثبت نام
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, verbose_name='fullname')
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    def __str__(self):
        return self.full_name

from django.conf import settings
from django.db import models

class OTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP for {self.user.username}"

    def is_expired(self):
        from datetime import timedelta
        from django.utils import timezone
        return timezone.now() > self.created_at + timedelta(minutes=5)
