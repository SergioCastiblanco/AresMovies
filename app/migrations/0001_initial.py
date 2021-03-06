# Generated by Django 3.0.5 on 2020-04-23 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('sinopsis', models.TextField(max_length=2000, null=True)),
                ('anio', models.IntegerField(null=True)),
                ('actores', models.TextField(max_length=2000, null=True)),
                ('duracion', models.IntegerField(null=True)),
                ('enCartelera', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculaCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='peliculascategoria', to='app.Categoria')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='peliculascategoria', to='app.Pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=2000)),
                ('fechaHora', models.DateTimeField()),
                ('activo', models.BooleanField(null=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comentarios', to='app.Pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comentarios', to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(null=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='calificaciones', to='app.Pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='calificaciones', to='app.User')),
            ],
        ),
    ]
