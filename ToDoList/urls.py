from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]


app_name = "ToDoList"
