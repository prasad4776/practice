from rest_framework import serializers
from .models import MyInfo, Countries


class MyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyInfo
        fields = ["name", "age", "mobile_no", "countries"]

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError("Age should be more than 18")
        return age

    def validate_mobile_no(self, mobile_no):
        if len(str(mobile_no)) != 10:
            raise serializers.ValidationError("Plz enter correct Mobile number")
        return mobile_no


class CountriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"
