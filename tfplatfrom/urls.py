from django.urls import path
from tfplatfrom.views import CoolestTenDistrictsAPIView, CompareTemperatureAPIView

urlpatterns = [
    path('coolest-ten-districts/', CoolestTenDistrictsAPIView.as_view(), name='coolest-ten-districts'),
    path('compare-temperature/', CompareTemperatureAPIView.as_view(), name='compare-temperature'),

]