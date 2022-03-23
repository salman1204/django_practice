# import json
# from wsgiref import headers

# from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def api_home(request, *args, **kwargs):

   serializer = ProductSerializers(data=request.data)

   if serializer.is_valid():
      print(serializer.data)
      data = serializer.data
      return JsonResponse(data)
