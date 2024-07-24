from django.shortcuts import render
from django.views.generic.list import ListView
from .models import todoModel

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = todoModel

