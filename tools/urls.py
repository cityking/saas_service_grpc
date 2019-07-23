from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload),
    path('send_message', views.send_message),
    ]

