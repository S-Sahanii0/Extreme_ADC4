from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  . import views
app_name="account"
urlpatterns = [ 
 path('',views.index,name="index"),  
 path('register/',views.userregister,name="register"),
 path('login/',views.userlogin,name="login"),
 path('sucess/',views.sucess,name="sucess"),
]