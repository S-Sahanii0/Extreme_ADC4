from django.conf.urls import url 
from django.urls import path
from . import views
app_name = "Asset"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('search/',views.search,name="search"),
    
]