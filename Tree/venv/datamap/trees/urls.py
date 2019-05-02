from django.urls import path,re_path
from . import views


app_name = 'trees'
urlpatterns =[
    #path('', views.index, name='initial'),
    #re_path('all/(?P<pk>[-\w]+)/', views.TreeList.as_view(), name='tree'),
    re_path('all/$', views.TreeList.as_view(), name='tree'),
    re_path('^create/$', views.TreeCreate.as_view(), name='create'),
    re_path('^table/$', views.tree_table, name='tree_table'),
    re_path('^filtered_tree_table/$', views.FilteredTreeTableView.as_view(), name='tree-table-filter'),
    re_path('^task-create/$', views.TaskCreate.as_view(), name='task-create'),
    re_path('^filtered_task_table/$', views.FilteredTaskTableView.as_view(), name='task-table-filter'),

]