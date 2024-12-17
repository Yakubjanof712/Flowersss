# gul/views.py
from django.shortcuts import render
from .models import Gullar, Turlar
from django.http import Http404

def home(request):
    gullar = Gullar.objects.all()
    return render(request, 'gul/home.html', {'gullar': gullar})

def barcha_gullar(request):
    gullar = Gullar.objects.all()
    return render(request, 'gul/barcha_gullar.html', {'gullar': gullar})

def gul_by_tur(request, tur_id):
    try:
        tur = Turlar.objects.get(id=tur_id)
        gullar = Gullar.objects.filter(turlar=tur)
    except Turlar.DoesNotExist:
        raise Http404("Turlar topilmadi")
    return render(request, 'gul/gul_by_tur.html', {'tur': tur, 'gullar': gullar})

def gul_detail(request, gul_id):
    try:
        gul = Gullar.objects.get(id=gul_id)
    except Gullar.DoesNotExist:
        raise Http404("Gul topilmadi")
    return render(request, 'gul/gul_detail.html', {'gul': gul})
