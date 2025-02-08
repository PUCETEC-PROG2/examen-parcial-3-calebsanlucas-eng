from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Album
from .forms import ArtistaForm, AlbumForm
# Create your views here

def inicio(request):
    return render(request, 'inicio.html')

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'listas_artistas.html', {'artistas': artistas})

def detalle_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'detalle_artista.html', {'artista': artista})

def crear_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm()
    return render(request, 'editar_artista.html', {'form': form})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'editar_artista.html', {'form': form})

def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    artista.delete()
    return redirect('lista_artistas')

def lista_albumes(request):
    albumes = Album.objects.all()
    return render(request, 'lista_albumes.html', {'albumes': albumes})

def detalle_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'detalle_album.html', {'album': album})

def crear_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm()
    return render(request, 'editar_album.html', {'form': form})

def editar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('lista_albumes')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'editar_album.html', {'form': form})

def eliminar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('lista_albumes')