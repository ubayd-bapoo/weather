import datetime
import requests

from django.conf import settings

# ------------------------------------------------------------------------------
class Controller(object):
    def __init__(self):
        self._today = datetime.datetime.today()

    def weather_info(self, locations):
        """
        Builindg a dict of the correct format for the data
        """

        locations_data = {}
        for location in locations:
            locations_data[location] = self.location_data(locations[location])

        return locations_data

    def location_data(self, location_gps):
        """
        Making request to Dark Sky
        """

        url = '%s/%s/%s' % (settings.API_URL, settings.API_KEY, location_gps)
        response = requests.get(url)
        data_cleaned = self.clean_data(response.json())

        return data_cleaned

    def clean_data(self, data):
        """
        Returning the formatted data
        """

        data_cleaned = {}

        try:
            data_cleaned['date'] = self._today.strftime('%Y-%m-%d')
            data_cleaned['type'] = data['currently']['icon']
            data_cleaned['temperature'] = data['currently']['temperature']
            data_cleaned['rain_prob'] = data['currently']['precipProbability']
            data_cleaned['description'] = data['currently']['summary']

            data_cleaned['wind'] = {}
            data_cleaned['wind']['speed'] = data['currently']['windSpeed']
            data_cleaned['wind']['bearing'] = data['currently']['windBearing']
            data_cleaned['wind']['gust'] = data['currently']['windGust']

            data_cleaned['latitude'] = data['latitude']
            data_cleaned['longitude'] = data['longitude']
        except:
            data_cleaned = data

        return data_cleaned

