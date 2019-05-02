from django.urls import path,re_path
from . import views


app_name = 'trees'
urlpatterns =[
    #path('', views.index, name='initial'),
    #re_path('all/(?P<pk>[-\w]+)/', views.TreeList.as_view(), name='tree'),
    re_path('all/$', views.TreeList.as_view(), name='tree'),
    re_path('^tree-create/$', views.TreeCreate.as_view(), name='tree-create'),
    #path('tree-edit/(\d+)/', views.TreeUpdate.as_view(), name='tree-edit'),
    re_path('^tree-edit/(?P<pk>\d+)/$', views.TreeUpdate.as_view(), name='tree-edit'),
    re_path('^table/$', views.tree_table, name='tree_table'),# not to be used
    re_path('^tree-table-filter/$', views.FilteredTreeTableView.as_view(), name='tree-table-filter'),
    re_path('^task-create/$', views.TaskCreate.as_view(), name='task-create'),
    re_path('^task-edit/(?P<pk>\d+)/$', views.TaskUpdate.as_view(), name='task-edit'),
    re_path('^task-table-filter/$', views.FilteredTaskTableView.as_view(), name='task-table-filter'),
]

