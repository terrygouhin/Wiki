from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("newentry", views.newentry, name = "newentry"),
    path("<str:entry>", views.GetEntry, name = "entry")
 ]

