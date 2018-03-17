from django.urls import path

from api import views

urlpatterns= [
    path('user_detail/', views.User_detail),
]