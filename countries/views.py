from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from .models import MyInfo, Countries
from .serializers import MyInfoSerializers, CountriesSerializers
import json


# Create your views here.


class MyInfoView(ListCreateAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializers

    def create(self, request, *args, **kwargs):

        json_data = json.load(request.data.get("data"))

        country = json_data.pop("countries")
        json_data["countries"] = []
        for c in country:
            c_obj = Countries.objects.create(country_name=c)
            json_data["countries"].append(c_obj.id)

        serializer = MyInfoSerializers(data=json_data)
        if serializer.is_valid():
            serializer.save()

        else:
            return JsonResponse({"errors": serializer.errors})

        return JsonResponse({"data": serializer.data})

    #
    # def create(self, request, *args, **kwargs):
    #     json_data = json.load(request.data.get("data"))
    #     json_data["countries"] = [1, 2, 3]
    #     serializer = MyInfoSerializers(data=json_data)
    #     if serializer.is_valid():
    #         myinfo = MyInfo.objects.create(name=json_data["name"], mobile_no=json_data["mobile_no"],
    #                                        age=json_data["age"])
    #
    #     else:
    #         return JsonResponse({"errors": serializer.errors})
    #
    #     country = json_data.pop("countries")
    #     for c in country:
    #         c_obj = Countries.objects.create(country_name=c)
    #         myinfo.countries.add(c_obj)
    #
    #     return JsonResponse({"data": serializer.data})


class CountriesView(ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializers
