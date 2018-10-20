from django.urls import path
from . import views
urlpatterns = [
    path('test', views.index),
    path('about', views.about),
    path('login', views.login),
]