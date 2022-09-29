from django.urls import path, include
from . import views

urlpatterns = [
    path("entertainment/", views.getEntertainmentNews, name="getEntertainment"),
    path("india/", views.getIndianNews, name="getIndia"),
    path("education/", views.getEducationNews, name="getEducation"),
    path("political/", views.getPoliticalNews, name="getPolitical"),
    path("cities/", views.getCitiesNews, name="getCities")
]