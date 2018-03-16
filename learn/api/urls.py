from django.urls import path

from api import views
urlpatterns = [
    #TODO 
    path('api/', views.User_detail),
]