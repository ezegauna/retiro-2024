from django.shortcuts import render
from .models import Frase
import random


def home(request):
    frases = Frase.objects.all()
    frase_aleatoria = random.choice(frases)
    return render(request, "home.html", {"frase_aleatoria": frase_aleatoria})
