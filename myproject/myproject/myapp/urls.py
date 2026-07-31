from django.urls import path
from .views import hello_world, current_time

urlpatterns = [
    path('hello/', hello_world),
    path('current_time/', current_time),
]