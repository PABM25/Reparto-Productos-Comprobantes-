from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import RepartoForm
from .models import Reparto


@login_required
def imprimir_comprobante(request):
    numero_venta = request.GET.get('numero_venta')
    if not numero_venta:
        return redirect('vista')

    reparto = Reparto.objects.filter(num_venta=numero_venta).first()
    if not reparto:
        return HttpResponse("Reparto no encontrado para el número de venta indicado.", status=404)

    lineas = [
        ('Cliente', reparto.nombre_cliente),
        ('Número de venta', reparto.num_venta),
        ('Número vendedor', reparto.num_vendedor),
        ('Nombre vendedor', reparto.nombre_vendedor),
        ('Fecha de venta', reparto.fecha_venta),
        ('Teléfono', reparto.telefono),
        ('Dirección', reparto.direccion),
        ('Artículos', reparto.articulos),
        ('Fecha de entrega', reparto.fecha_entrega),
        ('Fecha de retiro', reparto.fecha_retiro),
        ('Opción de entrega', reparto.get_opcion_entrega_display()),
        ('Opción de retiro', reparto.get_opcion_retiro_display()),
        ('Observación', reparto.observacion),
    ]
    comprobante = "\n".join(f"{etiqueta}: {valor if valor is not None else ''}" for etiqueta, valor in lineas)
    return HttpResponse(comprobante, content_type='text/plain; charset=utf-8')


@login_required
def home(request):
    if request.method == 'POST':
        form = RepartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista')
    else:
        form = RepartoForm()

    return render(request, 'app/home.html', {'form': form, 'mensaje': ''})


@login_required
def vista(request):
    numero_venta = request.GET.get('numero_venta')
    if numero_venta:
        repartos = Reparto.objects.filter(num_venta=numero_venta)
    else:
        repartos = Reparto.objects.order_by('-fecha_venta')[:1]  # la última venta

    if request.method == 'POST':
        reparto = repartos.first()
        if reparto:
            reparto.entregado = bool(request.POST.get('entregado'))
            reparto.save()

    return render(request, 'app/vista.html', {'repartos': repartos})


@login_required
@require_http_methods(['GET', 'POST'])
def eliminar_reparto(request, num_venta):
    """GET muestra la confirmación; solo un POST borra."""
    reparto = get_object_or_404(Reparto, num_venta=num_venta)
    if request.method == 'POST':
        reparto.delete()
        return redirect('vista')
    return render(request, 'app/confirmar_eliminar.html', {'reparto': reparto})


@login_required
@require_http_methods(['GET', 'POST'])
def modificar_reparto(request, num_venta):
    reparto = get_object_or_404(Reparto, num_venta=num_venta)
    if request.method == 'POST':
        form = RepartoForm(request.POST, instance=reparto)
        if form.is_valid():
            form.save()
            return redirect('vista')
    else:
        form = RepartoForm(instance=reparto)
    return render(request, 'app/modificar_reparto.html', {'form': form})
