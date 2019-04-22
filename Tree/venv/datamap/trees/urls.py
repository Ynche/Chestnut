from django.urls import path,re_path
from . import views


app_name = 'trees'
urlpatterns =[
    #path('', views.index, name='initial'),
    re_path('all/(?P<pk>[-\w]+)/', views.TreeList.as_view(), name='tree'),
    re_path('^create/$', views.TreeCreate.as_view(), name='create'),

]