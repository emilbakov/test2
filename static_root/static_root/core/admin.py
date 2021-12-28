from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import HuntSpot


admin.site.register(HuntSpot, LeafletGeoAdmin)
