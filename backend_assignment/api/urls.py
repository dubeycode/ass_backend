from django.urls import path
from .views import BogieChecksheetCreateView, WheelSpecificationListView

urlpatterns = [
    path('forms/bogie-checksheet', BogieChecksheetCreateView.as_view(), name='bogie-checksheet'),
    path('forms/wheel-specifications', WheelSpecificationListView.as_view(), name='wheel-specifications'),
]