from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderanOverview, name="orderan-overview"),
    path('orderan-list/', views.orderanlist, name="orderan-list"),
    path('orderan-detail/<str:pk>/', views.orderanDetail, name="orderan-detail"),
    path('orderan-create/', views.orderanCreate, name="orderan-create"),
    path('orderan-update/<str:pk>/', views.orderanUpdate, name="orderan-update"),
    path('orderan-delete/<str:pk>/', views.orderanDelete, name="orderan-delete"),
   
]
