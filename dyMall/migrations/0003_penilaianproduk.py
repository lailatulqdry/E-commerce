# Generated by Django 5.0.3 on 2024-05-06 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyMall', '0002_produk'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenilaianProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('komentar', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaianproduk', to='dyMall.produk')),
            ],
        ),
    ]
