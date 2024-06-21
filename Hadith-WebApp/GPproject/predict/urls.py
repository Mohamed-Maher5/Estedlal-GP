from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    # path('haraka/', views.haraka, name='haraka'),
        ]

