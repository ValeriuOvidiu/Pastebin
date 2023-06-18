from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path ("paste/create",views.createpost,name="paste/create"),
    path("paste/id/<int:id1>",views.layout,name="paste/id"),
]