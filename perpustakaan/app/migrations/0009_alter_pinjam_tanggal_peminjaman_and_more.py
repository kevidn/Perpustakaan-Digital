# Generated by Django 4.2.10 on 2024-02-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_pinjam_tanggal_peminjaman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjam',
            name='tanggal_peminjaman',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pinjam',
            name='tanggal_pengembalian',
            field=models.DateField(),
        ),
    ]
