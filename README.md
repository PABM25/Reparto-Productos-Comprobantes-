# Reparto-Productos-Comprobantes-

Claro, aquí tienes una propuesta de README para tu proyecto, generado a partir de los archivos que proporcionaste.

Reparto-Productos-Comprobantes
Este es un proyecto web desarrollado con Django, diseñado para gestionar y rastrear los repartos de productos y la generación de comprobantes asociados.

Descripción del Proyecto
La aplicación permite registrar información detallada sobre las ventas, incluyendo los datos del cliente, los artículos vendidos, y las opciones de entrega o retiro. El sistema está enfocado en facilitar la logística de despacho, permitiendo marcar repartos como "entregados" y gestionar la información de vendedores.

Características Principales
Gestión de Repartos: Creación, modificación y eliminación de registros de repartos.

Seguimiento de Ventas: Almacena el número de venta, fecha, cliente, dirección y artículos.

Opciones de Entrega: Soporta múltiples métodos de entrega, como "Retiro en Tienda" y "Reparto a domicilio".

Opciones de Retiro: Define lugares de retiro específicos como "Retiro Local" o "Retiro bodega".

Estado de Entrega: Permite marcar un reparto como entregado (verdadero/falso).

Impresión: Incluye una funcionalidad para "imprimir comprobante".

Seguridad: Utiliza python-decouple para gestionar variables sensibles (como SECRET_KEY y DEBUG) fuera del código fuente.

Tecnologías Utilizadas
El proyecto está construido principalmente con las siguientes tecnologías y librerías:

Backend: Python, Django

Base de Datos: SQLite (configuración por defecto)

Interfaz de Admin: django-admin-interface

Formularios: django-crispy-forms y crispy-bootstrap4

Configuración: python-decouple

Configuración e Instalación
Para ejecutar este proyecto localmente, sigue estos pasos:

Clonar el repositorio:

Bash

git clone [URL_DEL_REPOSITORIO]
cd Reparto-Productos-Comprobantes-
Crear y activar un entorno virtual:

Bash

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
.\venv\Scripts\activate
Instalar las dependencias: El archivo requeriments.txt lista todas las dependencias necesarias.

Bash

pip install -r requeriments.txt
Configurar variables de entorno: El proyecto usa python-decouple, por lo que necesitas crear un archivo .env en la raíz del proyecto (junto a manage.py).

Ini, TOML

# Archivo .env
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
DEBUG=True
Aplicar las migraciones: Esto creará la base de datos SQLite y las tablas necesarias para el modelo Reparto.

Bash

python manage.py migrate
Ejecutar el servidor de desarrollo:

Bash

python manage.py runserver
La aplicación estará disponible en http://127.0.0.1:8000/.
