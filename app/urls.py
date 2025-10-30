from django.urls import path
from .views import home, imprimir_comprobante, vista,  eliminar_reparto, modificar_reparto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('vista/', vista, name="vista"),
    path('eliminar-reparto/', eliminar_reparto, name="eliminar_reparto"),
    path('modificar-reparto/', modificar_reparto, name="modificar_reparto"),
    path('imprimir-comprobante/', imprimir_comprobante, name='imprimir_comprobante'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)