from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homecompagnie,name='homecompagnie'),
    path('<int:compagnie_id>', views.detailcompagnie,name='detailcompagnie'),
    path('<int:compagnie_id>/update', views.updatecompagnie,name='updatecompagnie'),
    
]