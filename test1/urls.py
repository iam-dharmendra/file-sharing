from django.http import HttpResponse
from  django.urls import path
from django.views.generic.base import View
from .import views 



urlpatterns=[
            path('',views.Deatilviews.as_view()),
            path('update/<int:id>/',views.UpdateDeatils.as_view()),
            path('store/',views.store),
            path('show/',views.showcsv.as_view()),
            path('put/<int:id>/',views.PutData.as_view()),
            path('read/',views.showall.as_view()),
            path('invoice/',views.Demoview.as_view())
            ]