from django.shortcuts import render, redirectfrom .models 
import Ciudad, Modelo, Propietario, Vehiculo
from django.contrib import messages


# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')  # Asegúrate de tener este template

# Vista para listar los propietarios
def propietario(request):
    propietariosBdd = Propietario.objects.all()
    return render(request, "propietario.html", {'propietarios': propietariosBdd})

# Vista para guardar un nuevo propietario
def guardarPropietario(request):
    nombre = request.POST["nombre_pro"]
    apellido = request.POST["apellido_pro"]
    correo = request.POST["email_pro"]
    telefono = request.POST["telefono_pro"]
    
    nuevoPropietario = Propietario.objects.create(
        nombre_pro=nombre,
        apellido_pro=apellido,
        email_pro=correo,
        telefono_pro=telefono
    )
    messages.success(request, "Propietario registrado exitosamente.")
    return redirect('propietario')  # Asegúrate de que 'propietario' esté definido en tus URLs

# Vista para mostrar el formulario de nuevo propietario
def nuevoPropietario(request):
    return render(request, 'nuevoPropietario.html')

# Vista para eliminar un propietario
def eliminarPropietario(request, id):
    propietarioEliminar = Propietario.objects.get(id=id)
    propietarioEliminar.delete()
    messages.success(request, "Propietario eliminado exitosamente.")
    return redirect('propietario')

# Vista para editar un propietario
def editarPropietario(request, id):
    propietarioEditar = Propietario.objects.get(id=id)
    return render(request, 'editarPropietario.html', {'propietarioEditar': propietarioEditar})

# Vista para actualizar un propietario
def actualizarPropietario(request):
    id = request.POST['id_pro']
    nombre = request.POST['nombre_pro']
    apellido = request.POST['apellido_pro']
    correo = request.POST['email_pro']
    telefono = request.POST['telefono_pro']
    
    
    propietarioActualizar = Propietario.objects.get(id=id)
    propietarioActualizar.nombre_pro = nombre
    propietarioActualizar.apellido_pro = apellido
    propietarioActualizar.email_pro_pro = correo
    propietarioActualizar.telefono_pro = telefono
    propietarioActualizar.save()
    
    messages.success(request, 'Propietario actualizado exitosamente.')
    return redirect('propietario')


# Vista para listar las ciudades
def ciudad(request):
    ciudadesBdd = Ciudad.objects.all()
    return render(request, "ciudad.html", {'ciudades': ciudadesBdd})

# Vista para guardar una nueva ciudad
def guardarCiudad(request):
    nombre = request.POST["nombre"]
    pais = request.POST["pais"]
    
    nuevaCiudad = Ciudad.objects.create(
        nombre=nombre,
        pais=pais
    )
    messages.success(request, "Ciudad registrada exitosamente.")
    return redirect('ciudad')

# Vista para mostrar el formulario de nueva ciudad
def nuevaCiudad(request):
    return render(request, 'nuevaCiudad.html')

# Vista para eliminar una ciudad
def eliminarCiudad(request, id):
    ciudadEliminar = Ciudad.objects.get(id=id)
    ciudadEliminar.delete()
    messages.success(request, "Ciudad eliminada exitosamente.")
    return redirect('ciudad')

# Vista para editar una ciudad
def editarCiudad(request, id):
    ciudadEditar = Ciudad.objects.get(id=id)
    return render(request, 'editarCiudad.html', {'ciudadEditar': ciudadEditar})

# Vista para actualizar una ciudad
def actualizarCiudad(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    pais = request.POST['pais']
    
    ciudadActualizar = Ciudad.objects.get(id=id)
    ciudadActualizar.nombre = nombre
    ciudadActualizar.pais = pais
    ciudadActualizar.save()
    
    messages.success(request, 'Ciudad actualizada exitosamente.')
    return redirect('ciudad')



# Vista para listar los modelos
def modelo(request):
    modelosBdd = Modelo.objects.all()
    return render(request, "modelo.html", {'modelos': modelosBdd})

# Vista para guardar un nuevo modelo
def guardarModelo(request):
    nombre = request.POST["nombre_mo"]
    placa = request.POST["placa_mo"]
    
    nuevoModelo = Modelo.objects.create(
        nombre_mo =nombre,
        placa_mo =placa
    )
    messages.success(request, "Modelo registrado exitosamente.")
    return redirect('modelo')

# Vista para mostrar el formulario de nuevo modelo
def nuevoModelo(request):
    return render(request, 'nuevoModelo.html')

# Vista para eliminar un modelo
def eliminarModelo(request, id):
    modeloEliminar = Modelo.objects.get(id=id)
    modeloEliminar.delete()
    messages.success(request, "Modelo eliminado exitosamente.")
    return redirect('modelo')

# Vista para editar un modelo
def editarModelo(request, id):
    modeloEditar = Modelo.objects.get(id=id)
    return render(request, 'editarModelo.html', {'modeloEditar': modeloEditar})

# Vista para actualizar un modelo
def actualizarModelo(request):
    id = request.POST['id']
    nombre = request.POST['nombre_mo ']
    placa = request.POST['placa_mo ']
    
    modeloActualizar = Modelo.objects.get(id=id)
    modeloActualizar.nombre_mo  = nombre
    modeloActualizar.placa_mo  = placa
    modeloActualizar.save()
    
    messages.success(request, 'Modelo actualizado exitosamente.')
    return redirect('modelo')