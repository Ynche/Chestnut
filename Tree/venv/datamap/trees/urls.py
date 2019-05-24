from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView


# app_name = 'trees'

urlpatterns =[
    #path('', views.index, name='initial'),
    #re_path('all/(?P<pk>[-\w]+)/', views.TreeList.as_view(), name='tree'),
    re_path('all/$', views.TreeList.as_view(), name='tree'),
    re_path('^tree-create/$', views.TreeCreate.as_view(), name='tree-create'),
    #path('tree-edit/(\d+)/', views.TreeUpdate.as_view(), name='tree-edit'),
    re_path('^tree-edit/(?P<pk>\d+)/$', views.TreeUpdate.as_view(), name='tree-edit'),
    re_path('^tree-delete/(?P<pk>\d+)/$', views.TreeDelete.as_view(), name='tree-delete'),
    re_path('^table/$', views.tree_table, name='tree_table'),# not to be used
    re_path('^tree-table-filter/$', views.FilteredTreeTableView.as_view(), name='tree-table-filter'),
    re_path('^task-create/$', views.TaskCreate.as_view(), name='task-create'),
    re_path('^task-edit/(?P<pk>\d+)/$', views.TaskUpdate.as_view(), name='task-edit'),
    re_path('^task-delete/(?P<pk>\d+)/$', views.TaskDelete.as_view(), name='task-delete'),
    re_path('^task-table-filter/$', views.FilteredTaskTableView.as_view(), name='task-table-filter'),
    re_path('^mytask-table-filter/$', views.MyFilteredTaskTableView.as_view(), name='mytask-table-filter'),
    re_path('^home-page/$', TemplateView.as_view(template_name='home-page.html')),
    re_path('^tree-download/$', views.export_csv_view, name='tree-download.html'),


]

