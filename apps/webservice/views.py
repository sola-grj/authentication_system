from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# @csrf_exempt
@login_required(login_url='/login/')
def view_index(request):
    """主页"""
    username = request.user.username
    return render(request, 'web_app/index.html', {'username': username if username else '未登录'})


def view_login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'web_app/user/login.html', {'msg': ""})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({
                'code': 0,
                'msg': 'success',
                'data': []
            })
        else:
            return render(request, 'web_app/user/login.html', {'msg': '用户名或密码错误'})


def view_register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'web_app/user/register.html', {'msg': ''})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        if user:
            return JsonResponse({
                'code': 0,
                'msg': 'success',
                'data': []
            })
        else:
            return render(request, 'web_app/user/login.html', {'msg': '系统错误'})


def view_logout(request):
    """退出"""
    logout(request)
    login_url = reverse('login')
    return redirect(login_url)
