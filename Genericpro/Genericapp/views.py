from django.shortcuts import render

# Create your views here.
from Genericapp .serializers import Empserializer
from rest_framework import generics
from Genericapp.models import Emp

class Genericview_List(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer

class Genericview_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer
