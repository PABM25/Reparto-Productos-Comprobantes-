import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Reparto


def crear_reparto(num_venta=100):
    return Reparto.objects.create(
        num_venta=num_venta,
        fecha_venta=datetime.date(2026, 1, 15),
        nombre_cliente='Cliente de prueba',
        articulos='Refrigerador',
        observacion='Sin observaciones',
    )


class AccesoTests(TestCase):
    def test_sin_sesion_redirige_al_login(self):
        for nombre, args in [('home', []), ('vista', []), ('eliminar_reparto', [1]), ('modificar_reparto', [1])]:
            respuesta = self.client.get(reverse(nombre, args=args))
            self.assertEqual(respuesta.status_code, 302, nombre)
            self.assertIn(reverse('login'), respuesta['Location'])

    def test_sin_sesion_no_se_puede_borrar(self):
        reparto = crear_reparto()
        self.client.post(reverse('eliminar_reparto', args=[reparto.num_venta]))
        self.assertTrue(Reparto.objects.filter(pk=reparto.pk).exists())


class RepartoTests(TestCase):
    def setUp(self):
        usuario = User.objects.create_user('vendedor', password='clave-de-prueba-123')
        self.client.force_login(usuario)
        self.reparto = crear_reparto()

    def test_eliminar_por_get_solo_muestra_confirmacion(self):
        respuesta = self.client.get(reverse('eliminar_reparto', args=[self.reparto.num_venta]))
        self.assertContains(respuesta, 'Confirmar Eliminación')
        self.assertTrue(Reparto.objects.filter(pk=self.reparto.pk).exists())

    def test_eliminar_por_post_borra(self):
        respuesta = self.client.post(reverse('eliminar_reparto', args=[self.reparto.num_venta]))
        self.assertRedirects(respuesta, reverse('vista'))
        self.assertFalse(Reparto.objects.filter(pk=self.reparto.pk).exists())

    def test_eliminar_inexistente_da_404(self):
        respuesta = self.client.post(reverse('eliminar_reparto', args=[9999]))
        self.assertEqual(respuesta.status_code, 404)

    def test_modificar_con_datos_invalidos_conserva_errores(self):
        respuesta = self.client.post(reverse('modificar_reparto', args=[self.reparto.num_venta]), {})
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.context['form'].errors)

    def test_imprimir_comprobante(self):
        respuesta = self.client.get(reverse('imprimir_comprobante'), {'numero_venta': self.reparto.num_venta})
        self.assertEqual(respuesta.status_code, 200)
        texto = respuesta.content.decode()
        self.assertIn('Cliente: Cliente de prueba', texto)
        self.assertIn('Artículos: Refrigerador', texto)

    def test_marcar_entregado(self):
        url = reverse('vista') + f'?numero_venta={self.reparto.num_venta}'
        self.client.post(url, {'entregado': 'on'})
        self.reparto.refresh_from_db()
        self.assertTrue(self.reparto.entregado)
