from django.urls import path
from .views import home, notes_list


urlpatterns = [
    path('home/', home),
    path('notes/', notes_list, name='notes_list'),
]