from django.db import models  # Importa el módulo models de Django para definir modelos de base de datos

opciones_entrega = [  # Lista de opciones de entrega con tuplas que contienen un número y una descripción
    (0, "Retiro en Tienda"),
    (1, "Reparto a domicilio")
]

opcion_retiro = [  # Lista de opciones de retiro con tuplas que contienen un número y una descripción
    (2, "Retiro Local"),
    (3, "Retiro bodega")
]

class Reparto(models.Model):  # Define un modelo llamado Reparto que hereda de models.Model
    opcion_entrega = models.IntegerField( choices=opciones_entrega, default="0")  # Campo CharField que representa la opción de entrega
    num_venta = models.IntegerField()  # Campo IntegerField que representa el número de venta
    fecha_venta = models.DateField()  # Campo DateField que representa la fecha de venta
    nombre_cliente = models.CharField(max_length=60)  # Campo CharField que representa el nombre del cliente
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    articulos = models.TextField(max_length=300)  # Campo TextField que representa los artículos
    fecha_entrega = models.DateField(blank=True, null=True)  # Modificamos el campo fecha_entrega
    fecha_retiro = models.DateField(blank=True, null=True)  # Campo DateField que representa la fecha de retiro
    opcion_retiro = models.IntegerField( choices=opcion_retiro, default="2")  # Campo CharField que representa la opción de retiro
    observacion = models.TextField(max_length=200)  # Campo TextField que representa la observación
    num_vendedor = models.IntegerField(blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=60, blank=True, null=True)

    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Reparto {self.num_venta}"