from django.urls import path
from . import views
urlpatterns =[
     path('', views.orders.as_view()),
     path('order-detail/<str:pk>', views.order_detail.as_view()),
     path('users/', views.UserList.as_view()),
     path('users/<int:pk>/', views.UserDetail.as_view()),
]