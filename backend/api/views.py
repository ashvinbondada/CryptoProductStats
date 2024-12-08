from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import InterestFormSerializer, ProductStatsSerializer
from .models import InterestForm, ProductStats
import requests  

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

# CreateApiView is for creating only we can use list
# when we are going to read also 
class InterestFormView(generics.CreateAPIView):
    serializer_class = InterestFormSerializer
    permission_classes  = [AllowAny]
    queryset = InterestForm.objects.all()

    def perform_create(self, serializer):
        if not serializer.is_valid():
            print(serializer.errors)

        product = serializer.validated_data.get('product')
        queryset = InterestForm.objects.filter(product=product)

        if queryset.exists():
            print(serializer.errors)
        interest_form = serializer.save() 
        print(interest_form)
        self.create_product_stats(interest_form.product)
    
    def create_product_stats(self, product):
        # https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductstats
        PRODUCT_STATS_URL = f'https://api.exchange.coinbase.com/products/{product}/stats'
        resp = None
        try:
            resp = requests.get(PRODUCT_STATS_URL)
        except:
            raise Exception
        
        if not resp:
            raise Exception
        
        data = resp.json()
        data["product"] = product

        product_stats_serializer = ProductStatsSerializer(data=data)
        if product_stats_serializer.is_valid():
            final = product_stats_serializer.save()
        else:
            raise Exception

        
class ListProductStatsView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer
    permission_classes = [AllowAny]
    queryset = ProductStats.objects.all() 
        

class DeleteProductStatsView(generics.DestroyAPIView):
    serializer_class = ProductStatsSerializer 
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.kwargs['pk']
        return ProductStats.objects.filter(id=id)    