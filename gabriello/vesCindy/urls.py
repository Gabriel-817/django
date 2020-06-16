from django.urls import path

from . import views
urlpatterns = [
    path('join', views.join, name="join"),
    path('vescindy', views.vescindy, name="vescindy"),
]