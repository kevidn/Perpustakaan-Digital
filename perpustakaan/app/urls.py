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

    # Auth.
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
