from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.hometrajet,name='hometrajet'),
    path('<int:trajet_id>', views.detailtrajet,name='detailtrajet'),
    
]