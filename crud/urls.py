from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('carro/<int:id_carro>/', views.vista_detalle, name='detalle'),
]