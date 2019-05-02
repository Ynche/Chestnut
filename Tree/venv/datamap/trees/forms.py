from django import forms
from .models import Tree,Task
from django.core.validators import RegexValidator
import django_tables2 as tables
from django_filters import FilterSet
import django_filters as django_filters
from bootstrap_datepicker_plus import DatePickerInput
from django.conf import settings
from datetime import date


#https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/docs/Walkthrough.rst

class TreeForm(forms.ModelForm):
    #kind = list(Tree.KIND_CHOICES)
    kind = forms.ChoiceField(choices=Tree.KIND_CHOICES)
    #type = list(Tree.TYPE)
    #type = forms.CharField(max_length=30, widget=forms.Select(choices=Tree.TYPE))
    type = forms.ChoiceField(choices=Tree.TYPE_CHOICES)
    latin_name = forms.CharField(required=False,validators=[RegexValidator(r'^([A-Z][a-z]+\s*){1,3}$',message='Use convention http://thorpetrees.com/advice/table-of-latin-common-names/'
    )], widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    #origin_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    origin_date = forms.DateField(required=False,input_formats=settings.DATE_INPUT_FORMATS,widget=DatePickerInput(options={"format": "mm/dd/yyyy","autoclose": True}))
    end_date = forms.DateField(required=False,input_formats=settings.DATE_INPUT_FORMATS,help_text="Use the following format", widget=forms.TextInput(attrs={'class':'form-control'}))
    lifecycle_status = forms.ChoiceField(choices=Tree.LIFECYCLE)
    size = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    district = list(Tree.DISTRICT_CHOICES)
    latitude = forms.DecimalField(required=True,min_value=-90,max_value=90,max_digits=7,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:41.40338')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))
    longitude = forms.DecimalField(required=True,min_value=-180,max_value=180,max_digits=8,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:2.17403')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model=Tree
        fields= ('kind','type','latin_name','description','origin_date','size','district','latitude','longitude')

# latitude is between - 90 and 90. longitude is between - 180 and 180.

class TreeTable(tables.Table):
    class Meta:
        model = Tree
        template_name = 'django_tables2/bootstrap.html'


class TreeFilter(django_filters.FilterSet):
    class Meta:
        model = Tree
        fields = ['kind','type','latin_name','description','origin_date','end_date','size','district','latitude','longitude']


class TaskForm(forms.ModelForm):
    task_type = forms.ChoiceField(choices=Task.TASK_TYPE_CHOICES)
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES)
    date_generated = forms.DateField(initial=date.today,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_completed = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,widget=forms.TextInput(attrs={'class':'form-control'}))
    generation = forms.ChoiceField(choices=Task.GENERATION_CHOICES)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    task_force = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.DecimalField(required=False,max_digits=8,decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=Task
        fields= ('task_type','status','date_generated','date_completed','generation','description','task_force','cost','trees')

class TaskTable(tables.Table):
    class Meta:
        model = Task
        template_name = 'django_tables2/bootstrap.html'


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['task_type','status','date_generated','date_completed','generation','description','task_force','cost','trees']

