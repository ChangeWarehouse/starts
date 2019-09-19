from django.shortcuts import render, HttpResponse, redirect, reverse
from Dis import models
# Create your views here.

from django import forms


class ResForm(forms.Form):
    username = forms.CharField(label='用户名:')
    name = forms.CharField(label='真是姓名:')
    phone = forms.CharField(label='手机号码:')
    password = forms.CharField(label='密码:')
    re_password = forms.CharField(label='确认密码:')


def register(request):
    form_obj = ResForm()
    if request.method == 'POST':
        form_obj = ResForm(data=request.POST)
    return render(request, 'register.html', {'form_obj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        pwd = request.POST.get('loginPassword')
        obj = models.User.objects.filter(username=username, password=pwd)
        if obj:
            return redirect(reverse('home'))

    return render(request, 'login.html')


def charts(request):
    return render(request, 'charts.html')


def index(request):
    return render(request, 'index1.html')


def home(request):
    return render(request, 'home.html')


def tables(request):

    dic = [
        {'name': '苹果', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '香蕉', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '梨子', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '橙子', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '橘子', 'price': 23, 'oringn': '红', 'quality': '优'}
    ]
    # obj = models.User.objects.get('name')
    return render(request, 'tables.html', {'dic': dic})


def mobile(request):
    dic = [
        {'name': '阿拉丁', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '香蕉', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '梨子', 'price': 23, 'oringn': '红', 'quality': '优'}, ]
    return render(request, 'tables.html', {'dic': dic})


def computer(request):
    dic = [
        {'name': '橙子', 'price': 23, 'oringn': '红', 'quality': '优'},
        {'name': '橘子', 'price': 23, 'oringn': '红', 'quality': '优'}
    ]
    return render(request, 'tables.html', {'dic': dic})


def modal(request):
    return render(request, 'mt.html')


def picture(request):
    return render(request, '')


def details(request):
    return render(request, 'details.html', {'dic': 1})


def pictur(request):

    return render(request, 'pictur.html')


def forms(request):
    return render(request, 'forms.html')


def test(request):
    ret = models.User.objects.all()
    print(ret, type(ret))
    # for i in ret:
    #     print(i.username)

    return render(request, 'test.html', {'ret': ret})


def upload(request):
    if request.method == 'POST':
        res = request.POST.get('username')
        ret = request.POST.get('picture')

        obj = request.FILES.get('picture')
        print(obj.name, obj.size)
        print(res)
    return render(request, 'upload.html')
