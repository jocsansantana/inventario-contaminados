from django.urls import path
from . import views

app_name = 'contaminados'

urlpatterns = [
    path('', views.contaminados_view, name='tabla_bultos'),
    path('exportar-excel/', views.exportar_contaminados_excel, name='exportar_excel'),
    path('eliminar/<int:pk>/', views.eliminar_bulto, name='eliminar_bulto'),
]