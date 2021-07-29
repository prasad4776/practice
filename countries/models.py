from django.db import models


# Create your models here.


class Countries(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class MyInfo(models.Model):
    name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    age = models.IntegerField()
    countries = models.ManyToManyField(Countries, related_name="info")

    def __str__(self):
        return self.name
