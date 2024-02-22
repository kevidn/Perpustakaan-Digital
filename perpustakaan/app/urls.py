from django.contrib import admin
from django.urls import path
from django.utils.text import slugify

from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings

from .views import *

urlpatterns = [
    path('', index, name='index'),

    # Buku.
    path('buku/', data_buku, name='data_buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/edit/<int:id_buku>', edit_buku, name='edit_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),

    # Kategori Buku.
    path('kategori/', data_kategori, name='data_kategori'),
    path('kategori/tambah/', tambah_kategori, name='tambah_kategori'),
    path('kategori/edit/<int:id_kategori>', edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:id_kategori>', hapus_kategori, name='hapus_kategori'),

    # Peminjaman Buku.
    path('pinjam/', data_peminjaman, name='data_peminjaman'),
    path('pinjam/pribadi/', data_peminjaman_pribadi, name='data_peminjaman_pribadi'),
    path('pinjam/tambah/', tambah_peminjaman, name='tambah_peminjaman'),
    path('pinjam/print/', print_peminjaman, name='print_peminjaman'),
    path('pinjam/edit/<int:id_pinjam>', edit_peminjaman, name='edit_peminjaman'),
    path('pinjam/hapus/<int:id_pinjam>', hapus_peminjaman, name='hapus_peminjaman'),
    path('pinjam/hapus/pribadi/<int:id_pinjam>', hapus_peminjaman_pribadi, name='hapus_peminjaman_pribadi'),

    # Koleksi Buku Pribadi.
    path('koleksi/', data_koleksi, name='data_koleksi'),
    path('koleksi/tambah/', tambah_koleksi, name='tambah_koleksi'),
    path('koleksi/hapus/<int:id_koleksi>', hapus_koleksi, name='hapus_koleksi'),

    # Koleksi Buku Pribadi.
    path('ulasan/', data_ulasan, name='data_ulasan'),
    path('ulasan/tambah/', tambah_ulasan, name='tambah_ulasan'),
    path('ulasan/edit/<int:id_ulasan>', edit_ulasan, name='edit_ulasan'),
    path('ulasan/hapus/<int:id_ulasan>', hapus_ulasan, name='hapus_ulasan'),

    # Auth.
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
]
