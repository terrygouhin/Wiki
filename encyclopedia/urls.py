from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="title")
 ]

"""
path("<str:entry>", views.entry, name="showEntry"),
path("wiki/<str:entry>", views.entry, name="showEntry")
"""    