from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:pk>/', views.news_edit, name='news_edit'),
    path('news_add_new', views.news_add_new, name='news_add_new'),
    path('news/<int:pk>/change/', views.news_change, name='news_change'),
    path('contact/', views.sendMessage, name='sendMessage'),
    path('onas/', views.onas, name='onas'),
    path('internistyczne/', views.internistyczne, name='internistyczne'),
    path('profilaktyczne/', views.profilaktyczne, name='profilaktyczne'),
    path('chirurgiczne/', views.chirurgiczne, name='chirurgiczne'),
    path('ortopedyczne/', views.ortopedyczne, name='ortopedyczne'),
    path('badania_lab/', views.badania_lab, name='badania_lab'),
    path('rtg_ekg/', views.rtg_ekg, name='rtg_ekg'),
    path('pielegnacja/', views.pielegnacja, name='pielegnacja'),
    path('paszporty/', views.paszporty, name='paszporty'),
    path('czipowanie/', views.czipowanie, name='czipowanie'),
    path('diety/', views.diety, name='diety'),

]
