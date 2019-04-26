from django import forms
from .models import Tree
from django.core.validators import RegexValidator
import django_tables2 as tables
from django_filters import FilterSet
import django_filters as django_filters



class TreeForm(forms.ModelForm):
    #kind = list(Tree.KIND_CHOICES)
    kind = forms.ChoiceField(choices=Tree.KIND_CHOICES)
    #type = list(Tree.TYPE_CHOICES)
    #type = forms.CharField(max_length=30, widget=forms.Select(choices=Tree.TYPE))
    type = forms.ChoiceField(choices=Tree.TYPE_CHOICES)
    latin_name = forms.CharField(required=False,validators=[RegexValidator(r'^([A-Z][a-z]+\s*){1,3}$',message='Use convention http://thorpetrees.com/advice/table-of-latin-common-names/'
    )], widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    age = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    size = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    district = list(Tree.DISTRICT_CHOICES)
    latitude = forms.DecimalField(required=True,min_value=-90,max_value=90,max_digits=7,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:41.40338')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))
    longitude = forms.DecimalField(required=True,min_value=-180,max_value=180,max_digits=8,decimal_places=5,validators=[RegexValidator(r'^\d+.\d{5}$',message='Example:2.17403')],
                                   widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model=Tree
        fields= ('kind','type','latin_name','description','age','size','district','latitude','longitude')

# latitude is between - 90 and 90.

# longitude is between - 180 and 180.

class TreeTable(tables.Table):
    class Meta:
        model = Tree
        template_name = 'django_tables2/bootstrap.html'


class TreeFilter(django_filters.FilterSet):
    class Meta:
        model = Tree
        fields = ['kind','type','latin_name','description','age','size','district','latitude','longitude']