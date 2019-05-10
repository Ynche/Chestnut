from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('signup/', views.update_profile, name='signup'),
    path('profile/', views.redirect_user, name='profile'),
    #re_path('profile/(?P<pk>\d+)/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),

]