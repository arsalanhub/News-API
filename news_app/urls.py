from django.urls import path, include
from . import views

urlpatterns = [
    path("entertainment/", views.getEntertainmentNews, name="getEntertainment")
]