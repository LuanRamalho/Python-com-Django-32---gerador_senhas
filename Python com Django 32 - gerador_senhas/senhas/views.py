import random
import string
from django.shortcuts import render
from .models import Senha

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def index(request):
    if request.method == "POST":
        tamanho = int(request.POST.get("tamanho", 12))
        if tamanho < 8:
            tamanho = 8
        elif tamanho > 40:
            tamanho = 40

        senha_gerada = gerar_senha(tamanho)
        Senha.objects.create(valor=senha_gerada)

    senhas = Senha.objects.all()
    contador = senhas.count()

    return render(request, "index.html", {"senhas": senhas, "contador": contador})
