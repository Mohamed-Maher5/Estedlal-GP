from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'), 
    path('answer/', views.answer, name='answer'),
    path('intermediate/', views.answer, name='intermediate'),
    path('delete-chat/', views.delete_chat, name='delete_chat'),
    path('haraka/', views.haraka, name='haraka'),
        ]
