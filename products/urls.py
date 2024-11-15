from django.urls import path
from .views import product_view,product_list
urlpatterns = [
    path('product',product_view),
    path('product_list/', product_list, name='product-list'),
]
