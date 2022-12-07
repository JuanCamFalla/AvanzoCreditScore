from django.contrib import admin
from django.urls import path
from deudores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deudores/', views.DeudorList, name='deudores'),
]