from django import forms  # Importa el módulo forms de Django para crear formularios
from .models import Reparto  # Importa el modelo Reparto

class RepartoForm(forms.ModelForm):  # Define una clase de formulario llamada RepartoForm que hereda de forms.ModelForm
    opciones_entrega = [  # Lista de opciones de entrega con tuplas que contienen un número y una descripción
        (0, "Retiro en Tienda"),
        (1, "Reparto a domicilio")
    ]

    opcion_retiro = [  # Lista de opciones de retiro con tuplas que contienen un número y una descripción
        (2, "Retiro Local"),
        (3, "Retiro bodega")
    ]

    opcion_entrega = forms.ChoiceField(choices=opciones_entrega, widget=forms.RadioSelect)  # Campo de opción de entrega en el formulario
    opcion_retiro = forms.ChoiceField(choices=opcion_retiro, widget=forms.RadioSelect)  # Campo de opción de retiro en el formulario
    
    entregado = forms.BooleanField(required=False, widget=forms.CheckboxInput)


    class Meta:  # Clase interna Meta que configura el formulario
        model = Reparto # Especifica el modelo asociado al formulario
        fields = (
            'num_venta',
            'fecha_venta',
            'nombre_cliente',
            'articulos',
            'opcion_entrega',
            'opcion_retiro',
            'fecha_retiro',
            'direccion',
            'telefono',
            'fecha_entrega',
            'observacion',
            'num_vendedor',
            'nombre_vendedor',
            'entregado',  # Agrega el nuevo campo 'entregado' al formulario
        )  # Especifica que se deben incluir todos los campos del modelo en el formulario
        
        widgets = {  # Configuración de widgets personalizados para algunos campos del formulario
            'fecha_venta': forms.DateInput(attrs={'type': 'date'}),  # Utiliza un widget de entrada de fecha con tipo 'date'
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),  # Utiliza un widget de entrada de fecha con tipo 'date'
            'fecha_retiro': forms.DateInput(attrs={'type': 'date'}),  # Utiliza un widget de entrada de fecha con tipo 'date'
             'entregado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Aplica una clase al campo entregado para el estilo
        }