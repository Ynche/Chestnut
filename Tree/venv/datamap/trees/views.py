from django.shortcuts import render
from .models import Tree
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import TreeForm
# Create your views here.


class TreeList(ListView):
    model = Tree
    template_name = 'list.html'

class TreeCreate(CreateView):
    model = Tree
    form_class = TreeForm
    template_name = 'create.html'
    success_url = '/trees/all/'