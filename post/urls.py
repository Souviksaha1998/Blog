from django.contrib import admin
from django.urls import path , include
from post import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login , name='login'),
    path('Signup', views.sign , name='signup'),
    path('blog', views.blog , name='blog'),
    path('logout_view', views.logout_view, name='logout'),
    path('query', views.query , name='query'),
    path('blogfull/<int:posts>', views.blogfull , name='blogfull'),
    
    
]
