from django.urls import path
from .views import MyInfoView, CountriesView

urlpatterns = [
    path("info", MyInfoView.as_view(), name="get_create_info"),
    path("countries", CountriesView.as_view(), name="get_create_countries")
]
