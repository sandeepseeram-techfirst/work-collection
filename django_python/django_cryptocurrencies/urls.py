from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('websocket/', views.ws_connect, name='ws_connect'),
    path('websocket/<str:symbol>/', views.ws_price, name='ws_price'),
]