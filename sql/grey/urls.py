from django.urls import path
from .views import *

urlpatterns=[path('create/',create_tables),
            path('insert/',insert_values),
            path('update/',update_values),
            path('delete/',delete_values),
            path('read/',read_values),
]