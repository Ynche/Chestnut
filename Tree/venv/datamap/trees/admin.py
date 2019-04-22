from django.contrib import admin
from .models import Tree
from .models import Task

# Register your models here.

admin.site.register(Tree)
admin.site.register(Task)