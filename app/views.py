from django.shortcuts import redirect, render
from .models import Reparto
from .forms import RepartoForm
from django.http import HttpResponse


def imprimir_comprobante(request):
    # Obtener el parámetro 'numero_venta' de los parámetros GET de la solicitud
    numero_venta = request.GET.get('numero_venta')

    # Si no se proporciona el 'numero_venta', redirigir de nuevo a la página de la vista
    if not numero_venta:
        return redirect('vista')

    # Intentar obtener el objeto 'reparto' con el 'numero_venta' proporcionado
    reparto = Reparto.objects.filter(num_venta=numero_venta).first()

    # Si no se encuentra el objeto 'reparto', devolver un mensaje de error
    if not reparto:
        return HttpResponse("Reparto no encontrado para el 'numero_venta' proporcionado.")

    # Renderizar el comprobante como una cadena de texto
    comprobante_texto = """
    Cliente: {}
    Número ticket: {}
    Número Vendedor: {}
    Número de Venta: {}
    Nombre Vendedor: {}
    Fecha de Venta: {}
    Teléfono: {}
    Dirección: {}
    Artículos: {}
    Fecha de Entrega: {}
    Fecha de Retiro: {}
    Opción de Entrega: {}
    Opción de Retiro: {}
    Observación: {}
    """.format(
        reparto.nombre_cliente,
        reparto.num_venta,
        reparto.fecha_venta,
        reparto.telefono,
        reparto.direccion,
        reparto.articulos,
        reparto.fecha_entrega,
        reparto.fecha_retiro,
        reparto.get_opcion_entrega_display(),
        reparto.get_opcion_retiro_display(),
        reparto.observacion,
        reparto.nombre_vendedor,
        reparto.num_vendedor
    )


    # Devolver una respuesta de éxito
    return HttpResponse("Comprobante impreso correctamente.")
        
        
def home(request):
    mensaje = ''
    if request.method == 'POST':
        form = RepartoForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            mensaje = '¡Formulario enviado correctamente!'
            # Redireccionar a una página de éxito (opcional)
            return redirect('vista')  # Reemplaza 'pagina_de_exito' con la URL a la que deseas redirigir después de guardar el formulario
        else:
            # Si hay errores en el formulario, puedes imprimirlos para depuración (opcional)
            print(form.errors)
    else:
        form = RepartoForm()

    context = {
        'form': form,
        'mensaje': mensaje,
    }
    return render(request, 'app/home.html', context)


def vista(request):
    numero_venta = request.GET.get('numero_venta')
    if numero_venta:
        repartos = Reparto.objects.filter(num_venta=numero_venta)
    else:
        repartos = Reparto.objects.order_by('-fecha_venta')[:1]  # Obtener la última compra

    if request.method == 'POST':
        entregado = request.POST.get('entregado')
        if entregado:
            # Si el checkbox está marcado, convertir el valor a True
            entregado = True
        else:
            # Si el checkbox no está marcado, convertir el valor a False
            entregado = False

        reparto = repartos.first()
        if reparto:
            # Actualizar el campo 'entregado' en el objeto Reparto
            reparto.entregado = entregado
            reparto.save()

    data = {
        'repartos': repartos
    }
    return render(request, 'app/vista.html', data)


def eliminar_reparto(request):
    numero_venta = request.GET.get('numero_venta')
    if numero_venta:
        reparto = Reparto.objects.filter(num_venta=numero_venta).first()
        if reparto:
            reparto.delete()
            return redirect('vista')

    # Si no se encuentra el reparto o no se proporciona un número de venta válido, redireccionar a la vista sin hacer nada
    return redirect('vista')

def modificar_reparto(request):
    numero_venta = request.GET.get('numero_venta')
    if numero_venta:
        reparto = Reparto.objects.filter(num_venta=numero_venta).first()
        if reparto:
            if request.method == 'POST':
                form = RepartoForm(request.POST, instance=reparto)
                if form.is_valid():
                    form.save()
                    return redirect('vista')

            form = RepartoForm(instance=reparto)
            return render(request, 'app/modificar_reparto.html', {'form': form})

    # Si no se encuentra el reparto o no se proporciona un número de venta válido, redireccionar a la vista sin hacer nada
    return redirect('vista')