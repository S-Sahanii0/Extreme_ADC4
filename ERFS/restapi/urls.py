from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = "restapi"

urlpatterns=[
   path('api/', views.api_dataall, name="api_dataall"),
   path('api/<int:pk>', views.api_dataspecific, name="api_dataspecific"),
   path('api/add', views.api_dataadd, name="api_dataadd"),
#    path('api/update/<int:pk>', views.api_update_data, name="api_update_data"),
#    path('api/delete/<int:pk>', views.api_delete_data, name="api_delete_data"),
#    path('api/page/<int:PAGENO>', views.api_food_pagination,
#         name="api_food_pagination"),


    
]