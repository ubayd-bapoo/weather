from django.db import models

# ==============================================================================
class Weather(models.Model):
    created = models.DateField(auto_now_add=True)

    date = models.DateTimeField(default=None, blank=True, null=True)
    latitude = models.CharField(default=None, max_length=250, null=True)
    longitude = models.CharField(default=None, max_length=250, null=True)

    type = models.CharField(default=None, max_length=250, null=True)
    temperature = models.FloatField(default=None, null=True)
    rain_prob = models.FloatField(default=None, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    wind_speed = models.FloatField(default=None, null=True)
    wind_bearing = models.FloatField(default=None, null=True)
    wind_gust = models.FloatField(default=None, null=True)

    def __str__(self):
        return str('%s: %s' % (self.latitude, self.longitude))
