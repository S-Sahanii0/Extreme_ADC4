from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  . import views
app_name="account"
urlpatterns = [ 
 path('',views.index,name="index"),  
 path('registerB/',views.registerB,name="registerB"),
 path('registerS/',views.registerS,name="registerS"),
 path('loginB/',views.loginB,name="loginB"),
 path('loginS/',views.loginS,name="loginS"),
 path('book/',views.book,name="book"),
 path('upload/',views.upload,name="upload"),
]