# Generated by Django 5.0.3 on 2024-05-13 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyMall', '0007_remove_produk_toko'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='toko',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='produk', to='dyMall.toko'),
        ),
    ]
