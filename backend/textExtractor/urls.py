from django.urls import path,include
from . import views

urlpatterns = [
    path('textExtractor/', views.textExtractor,name="textExtractor"),
    path('pdfTextExtractor/',views.pdfTextExtractor,name="pdfTextExtractor"),
]