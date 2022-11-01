from django.shortcuts import render, redirect
from . forms import todoform
from django.urls import reverse_lazy
from . models import Tasktable
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import todoform


# Create your views here..
class todoview(CreateView):
    model = Tasktable
    form_class = todoform
    template_name = 'home.html'
    success_url = 'home'
class Todolist(ListView):
    model = Tasktable
    template_name = 'home.html'
    context_object_name = 'task1'
class tododetail(DetailView):
    model=Tasktable
    template_name = 'detail.html'
    fields = ('name', 'priority', 'date')
    context_object_name = 'task1'

class Todoupdate(UpdateView):
    model = Tasktable
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class Tododelete(DeleteView):
    model = Tasktable
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

