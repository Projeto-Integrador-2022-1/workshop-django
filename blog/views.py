from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def perfil(request):
    return render(request, 'blog/perfil.html')
