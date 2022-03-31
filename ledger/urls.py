from os import name
from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
            path('ledger/',views.my),
            path('web/',views.web,name='web'),
            path('llogin/',views.llogin,name='llogin'),
            path('lsignup/',views.lSignup,name='lsignup'),
            path('llogout/',views.llogout,name='llogout1'),
            # path('home/',views.home, name='home'),
            # path('node_api/',views.node_api, name='node_api'),
          
]