#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/20
import re
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin

# 白名单
exclude_path = ["/login/", "/logout/", "/signup/", "/login_check/", "/static/","/admin/"]


# 验证用户是否登陆中间件(可选)
class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        url_path = request.path
        # print(url_path)
        # 如果请求在白名单里，则通过，不进行操作
        for each in exclude_path:
            if re.match(each, url_path):
                return None
        # 如果未登陆，则调转到登陆页面，将请求的url作为next参数
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect("/login/".format(url_path=url_path))
        # 如果已经登陆，则通过
        else:
            return None
