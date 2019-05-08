from django.shortcuts import render
from .models import Tree,Task
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import TreeForm,TreeTable,TreeFilter,TaskForm,TaskTable,TaskFilter
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# Create your views here.


class TreeList(ListView):
    model = Tree
    template_name = 'list.html'

class TreeCreate(CreateView):
    model = Tree
    form_class = TreeForm
    template_name = 'tree-create.html'
    success_url = '/trees/tree-table-filter/'

class TreeUpdate(UpdateView):
    model = Tree
    form_class = TreeForm
    template_name = 'tree-edit.html'
    success_url = '/trees/tree-table-filter/'


class TreeDelete(DeleteView):
    model = Tree
    template_name = 'tree-delete.html'
    success_url = '/trees/tree-table-filter/'


def tree_table(request):
    table = TreeTable(Tree.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tree_table.html', {'table': table})

#https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
#https://pypi.org/project/django-tables2-bootstrap4/
#https://django-tables2.readthedocs.io/en/latest/pages/filtering.html


class FilteredTreeTableView(SingleTableMixin, FilterView):
    table_class = TreeTable
    model = Tree
    template_name = 'tree-table-filter.html'
    filterset_class = TreeFilter

#https://django-filter.readthedocs.io/en/master/ref/filterset.html
#https://django-tables2.readthedocs.io/en/latest/pages/export.html - For exporting CSV

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-create.html'
    success_url = '/trees/task-table-filter/'

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-edit.html'
    success_url = '/trees/task-table-filter/'

class TaskDelete(DeleteView):
    model = Task
    template_name = 'task-delete.html'
    success_url = '/trees/task-table-filter/'

class FilteredTaskTableView(SingleTableMixin, FilterView):
    table_class = TaskTable
    model = Task
    template_name = 'task-table-filter.html'
    filterset_class = TaskFilter
    #table_pagination = {'per_page': 10} How should I use it?


