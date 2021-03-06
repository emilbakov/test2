
# Create your models here.
from django.db import models
from django.contrib.gis.db import models as geomodels
from djgeojson.fields import PointField


class HuntSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    geometry = geomodels.PointField(blank=True, null=True)
    geom = PointField(blank=True,null=True)

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
