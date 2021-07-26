from django.shortcuts import redirect, render 
from .models import Usuario
from .forms import UsuarioForm


def home(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'luna/home.html', context)


def agregar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()

    context = {'form': form}
    return render(request, 'luna/agregar.html', context)

def eliminar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect ("home")


def editar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm(instance=usuario)

    context = {'form': form}
    return render(request, 'luna/editar.html', context)