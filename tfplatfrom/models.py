from django.db import models


# Create your models here.
class District(models.Model):
    division_id = models.CharField()
    name = models.CharField(max_length=200)
    bn_name = models.CharField()
    lat = models.CharField()
    long = models.CharField()

    def __abs__(self):
        return self.name