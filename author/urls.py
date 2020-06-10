from django.urls import path
from django.conf.urls import url
from . import views
import re

from book.views import searchBook

app_name = 'author'

urlpatterns = [
    path('author/', views.index),

    path('', views.index , name='SiteIndex'),
    
    path('AllAuthors/', views.AllAuthors, name='AllAuthors'),
    path('<int:id>/', views.ReadAuthor, name='ReadAuthor'),
    path('<int:id>/edit', views.EditAuthor, name='EditAuthor'),

    path('create/', views.createAuthor, name='createAuthor'),

    path('<int:id>/delete/', views.DelAuthor, name='DelAuthor'),


    #path('searchBook/' , searchBook , name='searchBook') ,


    ]