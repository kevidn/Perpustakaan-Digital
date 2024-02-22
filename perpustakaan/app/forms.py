from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import Group

# Form tambah dan edit data buku.
class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({"class":"form-control"}),
            'penulis': forms.TextInput({"class":"form-control"}),
            'penerbit': forms.TextInput({"class":"form-control"}),
            'tahun_terbit': forms.NumberInput({"class":"form-control"}),
        }

# Form tambah dan edit data buku.
class FormKategori(ModelForm):   
    class Meta:
        model = Kategori
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({"class":"form-control"}),
        }

# Form tambah dan edit data peminjaman buku.
class FormPeminjaman(ModelForm):
    class Meta:
        model = Pinjam
        exclude = ('user', 'status', 'tanggal_peminjaman', )

        widgets = {
            'buku': forms.Select(choices=[('buku.id', 'buku.judul') for buku in Buku.objects.all()]),
            'tanggal_pengembalian': forms.DateInput(attrs={'type':'date'}),
        }

# Form tambah dan edit data peminjaman buku.
class FormUlasan(ModelForm):
    class Meta:
        model = Ulasan
        exclude = ('user', )

        widgets = {
            'buku': forms.Select(choices=[('buku.id', 'buku.judul') for buku in Buku.objects.all()]),
            'ulasan': forms.TextInput(),
            'rating': forms.NumberInput(attrs={'type':'number'}),
        }

# Form tambah dan edit data peminjaman buku.
class FormKoleksi(ModelForm):
    class Meta:
        model = Koleksi
        exclude = ('user', )

        widgets = {
            'buku': forms.Select(choices=[('buku.id', 'buku.judul') for buku in Buku.objects.all()]),
        }

# Form tambah user.
class SignUp(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

