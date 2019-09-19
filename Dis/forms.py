from django import forms
from Dis import models
import re


class RegForm(forms.Form):
    name = forms.CharField(max_length=10,min_length=3,label='用户名', error_messages={
        'required':'用户名不能为空!',
        'invalid':'格式错误！',
        'max_length':'注册用户名长度不能超过10位！',
        'min_length':'注册用户名长度不能低于3位',
    },
    widget=forms.widgets.Input(attrs={'class':'form-control','style':'width:250px'},))
    password = forms.CharField(max_length=16,min_length=3,label='密码', error_messages={
        'required':'注册密码不能为空！',
        'invalid':'格式错误！',
        'max_length':'密码超出最大长度16位！',
        'min_length':'密码长度不能低于3位！'
    },
    widget=forms.widgets.PasswordInput(attrs={'class':'form-control','style':'width:250px'})
    )
    re_password = forms.CharField(max_length=16, min_length=3,label='再次输入密码', error_messages={
        'required': '注册密码不能为空！',
        'invalid': '格式错误！',
        'max_length': '密码超出最大长度16位！',
        'min_length': '密码长度不能低于3位！'
    },
    widget=forms.widgets.PasswordInput(
       attrs={'class': 'form-control', 'style': 'width:250px'})
    )
    cellphone = forms.CharField(max_length=14,min_length=10,label='请输入手机号',error_messages={
        'required': '注册手机号不能为空！',
        'invalid': '格式错误！',
        'max_length': '手机号长度不合法！',
        'min_length': '手机号长度不合法！'
    },
    widget=forms.widgets.Input(attrs={'class':'form-control','style':'width:250px','id':'cellphone'})
    )
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            self.add_error('name','用户名必须由字母数字组成！')
        elif name[0].isdigit():
            self.add_error('name','用户名不能以数字开头！')
        elif models.User.objects.filter(name=name):
            self.add_error('name','该用户名已存在！')
        return name

    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            self.add_error('re_password','两次密码不一致！')
        elif password == '123':
            self.add_error('password','当前密码过于简单！')
        return self.cleaned_data
    def clean_cellphone(self):
        cellphone = self.cleaned_data.get("cellphone")
        regExp = "^((13[0-9])|(15[^4])|(18[0,2,3,5-9])|(17[0-8])|(147))\\d{8}$"
        if not re.findall(regExp,cellphone):
            self.add_error('cellphone','请输入正确的手机号！')
        elif models.User.objects.filter(cellphone = cellphone):
            self.add_error('cellphone','该手机号已注册！请换一个再试！')
        return cellphone
