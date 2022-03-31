
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
            path('signup/',views.SignupView,name='SIGNUP'),
            path('login/',views.userLogin,name='LOGIN'),
            path('logout/',views.userLogOut,name='LOGOUT'),   
            path('dash/', views.dashboard, name='DASHBOARD'),
          
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)