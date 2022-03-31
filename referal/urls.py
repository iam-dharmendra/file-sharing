
from django.http import HttpResponse
from  django.urls import path

from newwork.views import popup
from .views import * 



urlpatterns=[
            path('',hello),
            path('profiles/',my_reccomendation,name='my-recs-view'),
            path('all/',all),
            path('any/<str:ref_code>',any_recommendations_view),
            path('popup/',popup)
           
            ]