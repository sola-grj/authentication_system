#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/20

from django.urls import path, re_path
from apps.webservice import views

urlpatterns = [
    re_path('^index/$', views.view_index, name='index'),
    re_path('^login/$', views.view_login, name='login'),
    re_path('^register/$', views.view_register, name='register'),
    re_path('^logout/$', views.view_logout, name='logout'),
]
