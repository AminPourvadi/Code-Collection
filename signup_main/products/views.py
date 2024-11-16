from django.shortcuts import render
from .models import Products
# Create your views here.



def product_view(request):
    products = Products.objects.all()
    context={
        'massage':'my scarfs',
        'product':products,
    }
    return render(request,'products/products.html',context)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)
