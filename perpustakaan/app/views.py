from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils import timezone

from django.conf import settings

from .models import *
from .forms import *

# Create your views here.


# Signup page.
def signup(request):
    groups = Group.objects.all()
    if request.POST:
        form = SignUp(request.POST)
        if form.is_valid():
            form = form.save()

            messages.success(request, 'Akun berhasil dibuat!')

            return redirect('login')
    else:
        form = SignUp()

    all = {
        'title':'Sign Up',
        'form':form,
    }

    return render(request, 'registration/signup.html', all)

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
@permission_required('app.view_buku', login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_buku(request):
    data = Buku.objects.all()

    all = {
        'title':'Data Buku',
        'data':data,
    }

    return render(request, 'buku/data.html', all)

# Page untuk menambah buku.
@permission_required('app.add_buku',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data buku berhasil ditambahkan!')

            return redirect('data_buku')
    else:
        form = FormBuku()

    all = {
        'title':'Form Tambah Buku',
        'form':form,
    }

    return render(request, 'buku/tambah_data.html', all)

# Page untuk mengedit buku.
@permission_required('app.change_buku',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def edit_buku(request, id_buku):
    data = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST, instance=data)
        if form.is_valid():
            form.save()

            all = {
                'title':'Form Edit Data Buku',
                'data':data,
                'form':form,
            }

            return redirect('data_buku')
    else:
        form = FormBuku(instance=data)

    all = {
            'title':'Form Edit Data Buku',
            'data':data,
            'form':form,
        }

    return render(request, 'buku/edit_data.html', all)

# Untuk menghapus data buku.
@permission_required('app.delete_buku',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    data = Buku.objects.filter(id=id_buku)
    data.delete()

    return redirect('data_buku')

# Page untuk memperlihatkan data kategori.
@permission_required('app.view_kategori',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_kategori(request):
    data = Kategori.objects.all()

    all = {
        'title':'Data Kategori',
        'data':data,
    }

    return render(request, 'kategori/data.html', all)

# Page untuk menambah kategori.
@permission_required('app.add_kategori',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def tambah_kategori(request):
    if request.POST:
        form = FormKategori(request.POST)
        if form.is_valid():
            form.save()

            return redirect('data_kategori')
    else:
        form = FormKategori()

    all = {
        'title':'Form Tambah Kategori',
        'form':form,
    }

    return render(request, 'kategori/tambah_data.html', all)

# Page untuk mengedit kategori.
@permission_required('app.change_kategori',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def edit_kategori(request, id_kategori):
    data = Kategori.objects.get(id=id_kategori)
    if request.POST:
        form = FormKategori(request.POST, instance=data)
        if form.is_valid():
            form.save()

            all = {
                'title':'Form Edit Data Kategori',
                'data':data,
                'form':form,
            }

            return redirect('data_kategori')
    else:
        form = FormKategori(instance=data)

    all = {
            'title':'Form Edit Data Kategori',
            'data':data,
            'form':form,
        }

    return render(request, 'kategori/edit_data.html', all)

# Untuk menghapus data kategori.
@permission_required('app.delete_kategori',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_kategori(request, id_kategori):
    data = Kategori.objects.filter(id=id_kategori)
    data.delete()

    return redirect('data_kategori')

# Page untuk memperlihatkan data peminjaman.
@permission_required('app.view_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_peminjaman(request):
    data = Pinjam.objects.all()
    
    all = {
        'title':'Data Peminjaman Buku',
        'data':data,
    }

    return render(request, 'pinjam/data.html', all)

# Page untuk memperlihatkan data peminjaman pribadi.
@permission_required('app.view_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_peminjaman_pribadi(request):
    data = Pinjam.objects.filter(user=request.user)
    
    all = {
        'title':'Data Peminjaman Buku Pribadi',
        'data':data,
    }

    return render(request, 'pinjam/data_pribadi.html', all)

# Page untuk memperlihatkan data peminjaman.
@permission_required('app.view_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def print_peminjaman(request):
    data = Pinjam.objects.all()
    
    all = {
        'title':'Data Peminjaman Buku',
        'data':data,
    }

    return render(request, 'pinjam/print_data.html', all)

# Page untuk meminjam buku.
@permission_required('app.add_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def tambah_peminjaman(request, id_buku):
    buku = Buku.objects.get(pk=id_buku)
    if request.POST:
        form = FormPeminjaman(request.POST, instance=buku)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.status = 'Dipinjam'
            form.tanggal_peminjaman = timezone.now()

            form.save()

            return redirect('data_peminjaman_pribadi')
    else:
        form = FormPeminjaman(instance=buku)

    context = {
        'title': 'Form Peminjaman Buku',
        'form': form,
        'buku': buku,
    }

    return render(request, 'pinjam/tambah_data.html', context)

# Page untuk mengedit data peminjaman.
@permission_required('app.change_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def edit_peminjaman(request, id_peminjaman):
    data = Pinjam.objects.get(id=id_peminjaman)
    if request.POST:
        form = FormKategori(request.POST, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()

            all = {
                'title':'Form Edit Data Peminjaman',
                'data':data,
                'form':form,
            }

            return redirect('data_peminjaman')
    else:
        form = FormPeminjaman(instance=data)

    all = {
            'title':'Form Edit Data Peminjaman Buku',
            'data':data,
            'form':form,
        }

    return render(request, 'pinjam/edit_data.html', all)

# Untuk menghapus data peminjaman.
@permission_required('app.delete_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_peminjaman(request, id_pinjam):
    data = Pinjam.objects.filter(id=id_pinjam)
    data.delete()

    return redirect('data_peminjaman')

# Untuk menghapus data peminjaman.
@permission_required('app.delete_pinjam',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_peminjaman_pribadi(request, id_pinjam):
    data = Pinjam.objects.filter(id=id_pinjam)
    data.delete()

    return redirect('data_peminjaman_pribadi')

# Page yang berisi data koleksi.
@permission_required('app.view_koleksi',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_koleksi(request):
    data = Koleksi.objects.filter(user=request.user)

    all = {
        'title':'Data Koleksi Buku Pribadi',
        'data':data,
    }

    return render(request, 'koleksi/data.html', all)

# Page untuk menambah kategori.
@permission_required('app.add_koleksi',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def tambah_koleksi(request):
    if request.POST:
        form = FormKoleksi(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()

            return redirect('data_koleksi')
    else:
        form = FormKoleksi()

    all = {
        'title':'Form Tambah Koleksi',
        'form':form,
    }

    return render(request, 'koleksi/tambah_data.html', all) 

# Untuk menghapus data koleksi.
@permission_required('app.delete_koleksi',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_koleksi(request, id_koleksi):
    data = Koleksi.objects.filter(id=id_koleksi)
    data.delete()

    return redirect('data_koleksi')

# Page yang berisi ulasn.
@permission_required('app.add_ulasan',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def data_ulasan(request):
    data = Ulasan.objects.all()

    all = {
        'title':'Data Ulasan',
        'data':data,
    }

    return render(request, 'ulasan/data.html', all)

# Page untuk menambah ulasan.
@permission_required('app.view_ulasan',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def tambah_ulasan(request):
    if request.POST:
        form = FormUlasan(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('data_ulasan')
    else:
        form = FormUlasan()

    all = {
        'title':'Form Tambah Ulasan',
        'form':form,
    }

    return render(request, 'ulasan/tambah_data.html', all)

# Page untuk mengedit ulasan.
@permission_required('app.change_ulasan',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def edit_ulasan(request, id_ulasan):
    data = Ulasan.objects.get(id=id_ulasan)
    if request.POST:
        form = FormUlasan(request.POST, instance=data)
        if form.is_valid():
            form.save()

            all = {
                'title':'Form Edit Data Ulasan',
                'data':data,
                'form':form,
            }

            return redirect('data_ulasan')
    else:
        form = FormUlasan(instance=data)

    all = {
            'title':'Form Edit Data Ulasan',
            'data':data,
            'form':form,
        }

    return render(request, 'ulasan/edit_data.html', all)

# Untuk menghapus data ulasan.
@permission_required('app.delete_ulasan',login_url=settings.LOGIN_URL, raise_exception=True)
@login_required(login_url=settings.LOGIN_URL)
def hapus_ulasan(request, id_ulasan):
    data = Kategori.objects.filter(id=id_ulasan)
    data.delete()

    return redirect('data_ulasan')
