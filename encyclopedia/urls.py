from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.GetEntry, name="title"),
    path("css", views.css, name="css")
 ]

