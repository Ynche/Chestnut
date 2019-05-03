from django import forms
from .models import Tree,Task
from django.core.validators import RegexValidator
import django_tables2 as tables
from django_filters import FilterSet
import django_filters as django_filters
from bootstrap_datepicker_plus import DatePickerInput
from django.conf import settings
from datetime import date
from django_tables2.utils import A



#https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/docs/Walkthrough.rst

class TreeForm(forms.ModelForm):
    #kind = list(Tree.KIND_CHOICES)
    type = forms.ChoiceField(choices=Tree.TYPE_CHOICES, label="Type (required)")
    kind = forms.ChoiceField(choices=Tree.KIND_CHOICES, label="Kind (required)")
    #type = list(Tree.TYPE)
    #type = forms.CharField(max_length=30, widget=forms.Select(choices=Tree.TYPE))
    latin_name = forms.CharField(required=False,label="Latin Name (not required)",validators=[RegexValidator(r'^([A-Z][a-z]+\s*){1,3}$',message='Use convention http://thorpetrees.com/advice/table-of-latin-common-names/'
    )], widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(required=False, label="Description (not required)",widget=forms.Textarea(attrs={'class':'form-control'}))
    #origin_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    origin_date = forms.DateField(required=False,label="Origin Date (not required)",help_text="Format dd.mm.yyyy",input_formats=settings.DATE_INPUT_FORMATS,widget=DatePickerInput(options={"format": "mm/dd/yyyy","autoclose": True}))
    end_date = forms.DateField(required=False,input_formats=settings.DATE_INPUT_FORMATS,label="End Date (not required)",help_text="Format dd.mm.yyyy", widget=forms.DateInput(attrs={'class':'form-control'},format='%d.%m.%Y'))
    lifecycle_status = forms.ChoiceField(choices=Tree.LIFECYCLE,label="Lifecycle Status (required)")
    size = forms.IntegerField(required=False,label="Size (not required)",help_text="Grass/Flowers in sqm",widget=forms.TextInput(attrs={'class':'form-control'}))
    district = forms.ChoiceField(choices=Tree.DISTRICT_CHOICES,label="District (required)")
    latitude = forms.DecimalField(required=True,label="Latitude (required)",min_value=-90,max_value=90,max_digits=7,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:41.40338')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))
    longitude = forms.DecimalField(required=True,label="Longtitude (required)",min_value=-180,max_value=180,max_digits=8,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:2.17403')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model=Tree
        fields= ('type','kind','latin_name','description','origin_date','end_date','lifecycle_status','size','district','latitude','longitude')

# latitude is between - 90 and 90. longitude is between - 180 and 180.

class TreeTable(tables.Table):
    #edit = tables.LinkColumn('tree-update', text='Edit', args=[A('pk')], orderable=False, empty_values=())

    #def render_edit(self):
        #return 'Edit'
    #latin_name = tables.LinkColumn("tree-edit", args=[A("pk")], empty_values=()) #- Why this line of code does not work/tree-edit cannot be found???
    id = tables.TemplateColumn('<a href="/trees/tree-edit/{{record.id}}/">{{record.id}}</a>')
    origin_date = tables.DateColumn(format='d.m.Y')
    end_date = tables.DateColumn(format='d.m.Y')
    class Meta:
        model = Tree
        template_name = 'django_tables2/bootstrap.html'


class TreeFilter(django_filters.FilterSet):
    class Meta:
        model = Tree
        fields = ['kind','type','latin_name','description','origin_date','end_date','size','lifecycle_status','district','latitude','longitude']


class TaskForm(forms.ModelForm):
    task_type = forms.ChoiceField(choices=Task.TASK_TYPE_CHOICES,label="Type (required)")
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES,label="Status (required)")
    date_generated = forms.DateField(initial=date.today, localize=True, label="Date Generated (required)",help_text="Format dd.mm.yyyy Default is today but can be overwritten",input_formats=settings.DATE_INPUT_FORMATS,widget=forms.DateInput(attrs={'class':'form-control'},format='%d.%m.%Y'))
    date_completed = forms.DateField(required=False, label="Date Completed (not required)",help_text="Format dd.mm.yyyy",input_formats=settings.DATE_INPUT_FORMATS,widget=forms.DateInput(attrs={'class':'form-control'},format='%d.%m.%Y'))
    generation = forms.ChoiceField(choices=Task.GENERATION_CHOICES,label="Generation Type (required)")
    description = forms.CharField(required=False, label="Description (not required)",widget=forms.Textarea(attrs={'class':'form-control'}))
    task_force = forms.CharField(required=False, label="Task Force (not required)",widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.DecimalField(required=False,label="Cost (not required)",help_text="Format 12.34",max_digits=8,decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=Task
        fields= ('task_type','status','date_generated','date_completed','generation','description','task_force','cost','trees')

class TaskTable(tables.Table):
    id = tables.TemplateColumn('<a href="/trees/task-edit/{{record.id}}/">{{record.id}}</a>')
    date_generated = tables.DateColumn(format='d.m.Y')
    date_completed = tables.DateColumn(format='d.m.Y')
    class Meta:
        model = Task
        template_name = 'django_tables2/bootstrap.html'


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['task_type','status','date_generated','date_completed','generation','description','task_force','cost','trees']

