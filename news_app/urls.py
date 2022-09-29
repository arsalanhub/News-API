from django.urls import path, include
from . import views

urlpatterns = [
    path("entertainment/", views.getEntertainmentNews, name="getEntertainment"),
    path("india/", views.getIndianNews, name="getIndia")
]