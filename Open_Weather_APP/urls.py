from django.urls import path
from .views import CheckWeather

urlpatterns = [
    path('', CheckWeather.as_view(), name='weather_event'),
]