from django.http import HttpResponse
from django.shortcuts import render
from .models import Frase
import random


def home(request):
    if 'frase_cookie' in request.COOKIES:
        frase_aleatoria = request.COOKIES['frase_cookie']
    else:
        frases = Frase.objects.all()
        frase_aleatoria = random.choice(frases)
        response = HttpResponse()
        response.set_cookie('frase_cookie', frase_aleatoria)
    return render(request, "home.html", {"frase_aleatoria": frase_aleatoria})
