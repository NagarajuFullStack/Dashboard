from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import urls
from .views import *


app_name = 'basic_app'

urlpatterns = [
    # path('index/',index,name='index'),
    path('register/',register,name='register'),
    path('user_logout/',user_logout,name='user_logout'),
    path('userlogin/',userlogin,name='userlogin'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


