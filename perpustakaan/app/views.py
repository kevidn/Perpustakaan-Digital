from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from django.conf import settings

from .models import *
from .forms import *

# Create your views here.

# Index page.
@login_required(login_url=settings.LOGIN_URL)
def index(request):
    buku = Buku.objects.all()
    kategori = Kategori.objects.all()

    all = {
        'title':'Main Dashboard',
        'title_buku':'Data Buku',
        'buku':buku,
        'title_kategori':'Data Kategori',
        'kategori':kategori,
    }

    return render(request, 'main/index.html', all)

# Page untuk memperlihatkan data buku.
@login_required(login_url=settings.LOGIN_URL)
def data_buku(request):
    data = Buku.objects.all()

    all = {
        'judul':'Data Buku',
        'data':data,
    }

    return render(request, 'buku/data.html', all)

# Page untuk menambah buku.
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data buku berhasil ditambahkan!')

            return redirect('tambah_buku')
    else:
        form = FormBuku()

    all = {
        'title':'Form Tambah Buku',
        'form':form,
    }

    return render(request, 'buku/tambah_data.html', all)

# Page untuk mengedit buku.
@login_required(login_url=settings.LOGIN_URL)
def edit_buku(request, id_buku):
    data = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data buku berhasil diedit!')

            all = {
                'title':'Form Edit Data Buku',
                'data':data,
                'form':form,
            }

            return render(request, 'buku/edit_data.html', all)
    else:
        form = FormBuku(instance=data)

    all = {
            'title':'Form Edit Data Buku',
            'data':data,
            'form':form,
        }

    return render(request, 'buku/edit_data.html', all)

# Untuk menghapus data buku.
@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    data = Buku.objects.filter(id=id_buku)
    data.delete()

    return redirect('data_buku')

# Page untuk memperlihatkan data kategori.
@login_required(login_url=settings.LOGIN_URL)
def data_kategori(request):
    data = Kategori.objects.all()

    all = {
        'judul':'Data Kategori',
        'data':data,
    }

    return render(request, 'kategori/data.html', all)

# Page untuk menambah kategori.
@login_required(login_url=settings.LOGIN_URL)
def tambah_kategori(request):
    if request.POST:
        form = FormKategori(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kategori berhasil ditambahkan!')

            return redirect('tambah_kategori')
    else:
        form = FormKategori()

    all = {
        'title':'Form Tambah Kategori',
        'form':form,
    }

    return render(request, 'kategori/tambah_data.html', all)

# Page untuk mengedit kategori.
@login_required(login_url=settings.LOGIN_URL)
def edit_kategori(request, id_kategori):
    data = Kategori.objects.get(id=id_kategori)
    if request.POST:
        form = FormKategori(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kategori berhasil diedit!')

            all = {
                'title':'Form Edit Data Kategori',
                'data':data,
                'form':form,
            }

            return render(request, 'kategori/edit_data.html', all)
    else:
        form = FormKategori(instance=data)

    all = {
            'title':'Form Edit Data Kategori',
            'data':data,
            'form':form,
        }

    return render(request, 'kategori/edit_data.html', all)

# Untuk menghapus data kategori.
@login_required(login_url=settings.LOGIN_URL)
def hapus_kategori(request, id_kategori):
    data = Kategori.objects.filter(id=id_kategori)
    data.delete()

    return redirect('data_kategori')
