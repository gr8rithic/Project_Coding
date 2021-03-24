from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hel, name="helo"),
    path('subtract', views.add , name="add"), 
]

