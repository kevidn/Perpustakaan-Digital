from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({"class":"form-control"}),
            'penulis': forms.TextInput({"class":"form-control"}),
            'penerbit': forms.TextInput({"class":"form-control"}),
            'tahun_terbit': forms.TextInput({"class":"form-control"}),
        }

class FormKategori(ModelForm):   
    class Meta:
        model = Kategori
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({"class":"form-control"}),
        }

