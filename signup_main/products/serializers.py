from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'  # یا می‌توانید لیستی از فیلدها را اینجا مشخص کنید
