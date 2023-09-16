
from .views import *
from django.urls import  path

urlpatterns = [
    path("get-product", GetProductApiView.as_view(), name="get-product")

]