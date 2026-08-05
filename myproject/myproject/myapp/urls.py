from django.urls import path
from .views import hello_world, current_time, greet, calculator, show_files,show_headers, random_number, book_list

urlpatterns = [
    path('hello/', hello_world),
    path('current_time/', current_time),
    path('greet/<username>/', greet),
    path('calculator/<int:num1>/<str:operation>/<int:num2>', calculator),
    path('show/', show_files),
    path('show/<path:directory>/', show_files),
    path('headers/', show_headers),
    path('random/', random_number),
    path('random/<int:min_num>/<int:max_num>/', random_number),
    path('books/', book_list, name='book_list'),
]

