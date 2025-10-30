from django.urls import path
from . import views  # Es mejor importar 'views' así

urlpatterns = [
    path('', views.home, name="home"),
    path('vista/', views.vista, name="vista"),
    
    # --- MEJORA DE SEGURIDAD: Usar <int:num_venta> en la URL ---
    path('eliminar-reparto/<int:num_venta>/', views.eliminar_reparto, name="eliminar_reparto"),
    path('modificar-reparto/<int:num_venta>/', views.modificar_reparto, name="modificar_reparto"),
    # --- FIN DE MEJORA ---
    
    path('imprimir-comprobante/', views.imprimir_comprobante, name='imprimir_comprobante'),
]

