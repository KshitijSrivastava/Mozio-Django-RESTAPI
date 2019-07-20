from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from mozio.serializers import ProviderSerializer
from mozio.models import Provider

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Mozio REST API')

class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
