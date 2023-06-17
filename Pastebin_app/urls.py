from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path ("createpost",views.createpost,name="createpost"),
    path("layout/<int:id1>",views.layout,name="layout"),
]