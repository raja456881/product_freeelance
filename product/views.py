from django.shortcuts import render
from rest_framework.views import APIView
from .searilizers import ProductSearilizers
from .models import Product
from rest_framework.response import Response
from rest_framework import status
# Create your views he


class GetProductApiView(APIView):
    def post(self, request):
        product_data=Product.objects.all()
        searilizers=ProductSearilizers(product_data, many=True)

        return Response({"data":searilizers.data}, status=status.HTTP_400_BAD_REQUEST)


