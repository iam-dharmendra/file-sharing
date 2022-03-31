"""newwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls.conf import include

from CA.models import PrsignUp
from .views import main_view,signup_view
from referal.views import my_reccomendation
from CA.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsonxml/',include('jsonxml.urls')),
    path('test1/',include('test1.urls')),
    path('referal/',include('referal.urls')),
    path('',main_view,name='main-view'),
    path('signup/',signup_view,name='signup-view'),
    # path('<str:ref_code>/',main_view,name='main-view'),
    path('<str:ref_code>/',prSignupView,name='refprsignup'),
    path('ca/',include('CA.urls')),
    path('share/',include('share.urls')),
    path('share2/',include('share2.urls')),
    path('ledger/',include('ledger.urls')),
    
]
