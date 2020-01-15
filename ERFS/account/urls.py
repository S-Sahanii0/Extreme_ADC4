from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  . import views
app_name="account"
urlpatterns = [ 
 path('',views.index,name="index"),  
 path('register/',views.register,name="register"),
 path('login/',views.login,name="login"),
 path('logout/',views.logout,name="logout"),
]