"""PBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from django.http import HttpRequest
from PBE import views
from post.api.router import router_post

def otro(request):
    return HttpResponse('otro')
def otraView(request):
    return HttpResponse('Holaa')
def requestTest(request):
    return(HttpRequest.body)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('requestTest',requestTest),
    path('api/',include(router_post.urls))
  

]
