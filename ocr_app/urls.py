from django.urls import path
from . import views

urlpatterns = [
    path('', views.ocr_test, name='ocr_test'),
]
