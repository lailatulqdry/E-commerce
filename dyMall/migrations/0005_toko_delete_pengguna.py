# Generated by Django 5.0.3 on 2024-05-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyMall', '0004_pengguna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namatoko', models.CharField(max_length=20)),
                ('alamattoko', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pengguna',
        ),
    ]