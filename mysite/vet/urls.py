from django.urls import path
from . import views

urlpatterns = [
    path('', views.vet, name='vet'),
    path('contact/', views.sendMessage, name='sendMessage'),
    path('onas/', views.onas, name='onas'),

]