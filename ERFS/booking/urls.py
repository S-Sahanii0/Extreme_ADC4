from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = "booking"

urlpatterns=[
    path('assets/booking', views.upload, name="files"),
    path('booking', views.display, name="display"),
    path('booking/delete/<int:pk>/', views.delete_asset, name="delete_asset"),
    path('booking/update/<int:id>/', views.update_asset, name="update_asset" ),
    path('booking/favorites/<int:id>/', views.fav_list, name="fav_list" ),
    path('booking/booked/<int:pk>/', views.book_asset, name="book_asset"),
    
]