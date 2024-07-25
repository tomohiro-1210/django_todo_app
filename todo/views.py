from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import todoModel
from django.urls import reverse_lazy

# Create your views here.

# List(一覧画面)
class TodoList(ListView):
    template_name = 'list.html'
    model = todoModel

# Detail(詳細画面)
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = todoModel

# Create（登録、作成）
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = todoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')
