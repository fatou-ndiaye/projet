from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('<int:vol_id>', views.detail,name='detail'),
    path('<int:vol_d>/listcompagnie', views.listcomp,name='listcomp'),
    path('<int:vol_d>/supvol', views.supvol,name='supvol'),
]