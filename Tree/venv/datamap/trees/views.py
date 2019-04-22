from django.shortcuts import render
from .models import Tree
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import TreeForm,TreeTable
from django_tables2 import RequestConfig
# Create your views here.


class TreeList(ListView):
    model = Tree
    template_name = 'list.html'

class TreeCreate(CreateView):
    model = Tree
    form_class = TreeForm
    template_name = 'create.html'
    success_url = '/trees/all/'

def tree_table(request):
    table = TreeTable(Tree.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tree_table.html', {'table': table})
#https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
#https://pypi.org/project/django-tables2-bootstrap4/
#https://django-tables2.readthedocs.io/en/latest/pages/filtering.html