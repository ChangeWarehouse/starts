"""Display URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from Dis import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'register/', views.register,name='register'),
    url(r'login/', views.login,name='login'),
    url(r'charts/', views.charts,name = 'charts'),
    url(r'home/', views.home,name = 'home'),
    url(r'tables/', views.tables,name = 'tables'),
    url(r'forms/', views.forms,name = 'forms'),
    url(r'^$', views.tables,name = 'forms'),
    url(r'upload/', views.upload,name = 'upload'),
    url(r'mobile/', views.mobile,name = 'mobile'),
    url(r'computer/', views.computer,name = 'computer'),
    url(r'modal/', views.modal,name = 'modal'),
    url(r'details/', views.details,name = 'details'),
    url(r'pictur/', views.pictur,name = 'pictur'),
    # url(r'test/', views.test,name = 'test'),
]
