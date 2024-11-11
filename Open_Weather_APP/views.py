import requests
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import WeatherSerializer

from dotenv import load_dotenv
import os
load_dotenv()
API_Key = os.getenv('APIKEY')
# Create your views here.
#get the weather data from API




class CheckWeather(CreateAPIView):
    serializer_class = WeatherSerializer
#we use create method under createapiview
    def create(self, request, *args, **kwargs):
        #get data
        serializer = self.get_serializer(data=request.data)
        #we ensure data is serialized
        if serializer.is_valid():
            location = serializer.validated_data['location']
            weather_data = self.get_weather(location)
            if weather_data:
                response_data = {
                'location':location,
                'forecast': weather_data['weather'][0]['description'],
                'temperature': weather_data['main']['temp'],
                'condition': weather_data['weather'][0]['main'],
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
            }
                return Response({"Details:":response_data},status=status.HTTP_200_OK)
            else:
                return {}
        else:
            return {}
        # here, we get the api
    def get_weather(self, location):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_Key}&units=metric'
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None