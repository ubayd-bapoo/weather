from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Weather

from apis.controller import Controller

# ------------------------------------------------------------------------------
class weather(APIView):

    def get(self, request):
        #Getting locations from request
        locations = {}
        locations['current_location'] = request.query_params['current_location']
        locations['booking_location'] = request.query_params['booking_location']

        weather_contr = Controller()
        data = weather_contr.weather_info(locations)  # Making request to Dark Sky and cleaning data

        for location in data:
            if 'code' in data[location].keys():
                # If there's an error return the error and correct error code
                return Response(data, status=400, template_name=None, headers=None, content_type=None)

            # Saving data into DB
            weather_info, created = Weather.objects.get_or_create(
                                                                date=data[location]['date'],
                                                                latitude=data[location]['latitude'],
                                                                longitude=data[location]['longitude']
                                                                )

            if created:
                # If seeing data for the first time save it.
                weather_info.type = data[location]['type']
                weather_info.temperature = data[location]['temperature']
                weather_info.rain_prob = data[location]['rain_prob']
                weather_info.description = data[location]['description']

                weather_info.wind_speed = data[location]['wind']['speed']
                weather_info.wind_bearing = data[location]['wind']['bearing']
                weather_info.wind_gust = data[location]['wind']['gust']
                weather_info.save()

        return Response(data, status=200, template_name=None, headers=None, content_type=None)
