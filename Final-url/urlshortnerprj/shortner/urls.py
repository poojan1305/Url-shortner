from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shorten', views.shorten, name="shorten"),
    path('create', views.create, name="create"),
    path('<str:pk>', views.search, name="search")
   
]