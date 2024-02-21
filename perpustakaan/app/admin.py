from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Buku)
admin.site.register(Kategori)
admin.site.register(Ulasan)
admin.site.register(Koleksi)
admin.site.register(Pinjam)