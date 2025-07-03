from django.shortcuts import render, HttpResponse
from .models import Berita


def homepage(request):
    daftar_berita = Berita.objects.all()    
    context_data  = {
        'daftar_berita': daftar_berita,
    }
    return render(request, 'frontend/sections/homepage.html', context=context_data)


def tampilkan_berita(request, id):
    berita = Berita.objects.get(id = id)
    context_data  = {
        'berita': berita,
    }
    return render(request, 'frontend/sections/tampilkan_berita.html', context=context_data)
    