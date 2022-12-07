from django.contrib import admin
from django.urls import path
from deudores import views

urlpatterns = [
    path('deudores/', views.DeudorList, name='deudores'),
]