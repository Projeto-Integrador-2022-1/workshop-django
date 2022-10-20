from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from blog.forms import CadastraUsuario

# Create your views here.
def home(request):
    form = CadastraUsuario(request.POST)

    if request.method == "POST":
        if form.is_valid():
            if form.cleaned_data['confirma_senha'] == form.cleaned_data['password']:
                
               novo_usuario =  form.save()
               novo_usuario.password = make_password(form.cleaned_data['password'])
               novo_usuario.save()
            else:
                form.add_error("confirma_senha", "Você digitou senhas diferentes.")

    todos_os_usuarios = models.User.objects.all()

    contexto = {
        "cadastra_form": form,
        "todos": todos_os_usuarios,
    }

    return render(request, 'blog/index.html', context=contexto)

def perfil(request):
    return render(request, 'blog/perfil.html')
