from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# Model buku
class Buku(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    tahun_terbit = models.IntegerField()
    kategori = models.ManyToManyField('Kategori')

    def __str__(self):
        return self.judul

# Model kategori buku.
class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
        
# Model ulasan.
class Ulasan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)
    ulasan = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.buku.judul}'

# Model koleksi.
class Koleksi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.buku.judul}'

# Model peminjaman.
class Pinjam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey('Buku', on_delete=models.CASCADE)
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.buku.judul}'