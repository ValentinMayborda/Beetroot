from django.http import HttpResponse
from django.shortcuts import render
from .models import Note, Category


# def home(request):
#     return HttpResponse("Hello from Notes app")

def home(request):
    context = {
        'task1': "Переглянути перший урок по Django",
        'task2': "Зробити домашнє завдання",
        'task3': "Вивчати шаблони Django",
        'task4': "Створити моделі",
        'task5': "Додати функціонування",

    }

    return render(request, 'index.html', context)


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})