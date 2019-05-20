#from django import forms
from .models import ProfileUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email')

# class ProfileUserForm(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = ProfileUser
#         fields = ('username', 'password','email')