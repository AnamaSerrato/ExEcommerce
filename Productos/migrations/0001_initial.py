# Generated by Django 3.0.8 on 2021-09-23 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoElectrodomestico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('calificacion', models.FloatField(default=0)),
                ('marca', models.CharField(default='', max_length=20)),
                ('ref', models.CharField(default='', max_length=100)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.TipoElectrodomestico')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.FloatField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Perfil')),
            ],
        ),
    ]
