from django.shortcuts import render
from rest_framework import generics
from .models import BogieChecksheetForm, WheelSpecificationForm
from .serializers import BogieChecksheetFormSerializer, WheelSpecificationFormSerializer
# Create your views here.


#  POST /api/forms/bogie-checksheet
class BogieChecksheetCreateView(generics.CreateAPIView):
    queryset = BogieChecksheetForm.objects.all()
    serializer_class = BogieChecksheetFormSerializer

#  GET /api/forms/wheel-specifications
class WheelSpecificationListView(generics.ListAPIView):
    queryset = WheelSpecificationForm.objects.all()
    serializer_class = WheelSpecificationFormSerializer
