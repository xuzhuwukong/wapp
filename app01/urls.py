#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = David
# email:
from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.main_base_view, name='main_base'),
path("login/", views.login, name="myLog"),
path('addbook/', views.addbook),
path('add/', views.add),
path('books/', views.books),
re_path(r'books/(\d+)/delete', views.delbook),  # delbook(request,位置参数)
re_path(r'books/(\d+)/change', views.changebook),  # delbook(request,位置参数)
re_path(r'query', views.query)  # delbook(request,位置参数)
]