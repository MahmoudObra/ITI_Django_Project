from django.urls import path
from django.conf.urls import url
from . import views
import re

app_name = 'book'

urlpatterns = [
    path('book/', views.index),
    
    path('', views.AllBooks, name='AllBooks'),
    path('<int:id>/', views.ReadBook, name='ReadBook'),
    path('<int:id>/edit', views.EditBook, name='EditBook'),

    path('create/', views.createBook, name='createBook'),

    path('<int:id>/delete/', views.DelBook, name='DelBook'),

    path('searchBook/', views.searchBook, name='searchBook'),

    ]