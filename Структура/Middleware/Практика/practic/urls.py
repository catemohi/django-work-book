from django.urls import path
from practic import views

urlpatterns = [
    path('', views.index),
]