from django.http import HttpResponse
def testing (request):
    return HttpResponse('testeando app')
def algunaotracosa(request):
    return HttpResponse('hola')
"""
URL configuration for proyectpPBE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from PBE import views

def otro(request):
    return HttpResponse ('otro')
def otraView(request):
    return HttpResponse ('otraView')




urlpatterns =[
    path('admin/', admin.site.urls),
    path('testing/', views.testing),
    path('otracosa/', views.algunaotracosa),
    path ('otro/', otro),    
]