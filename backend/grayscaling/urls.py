from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.grayscale_conversion, name='grayscale_conversion'),
]