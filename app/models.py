from django.db import models
from django.contrib.auth.models import User


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    sinopsis = models.TextField(max_length=2000,null=True)
    anio = models.IntegerField(null=True)
    actores = models.TextField(max_length=2000,null=True)
    duracion = models.IntegerField(null=True)
    enCartelera = models.BooleanField(null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'app'
    

class Calificacion(models.Model):
    valor = models.IntegerField(null=True)
    usuario = models.ForeignKey(
        User,
        related_name='calificaciones',
        on_delete=models.PROTECT
    )
    pelicula = models.ForeignKey(
        Pelicula,
        related_name='calificaciones',
        on_delete=models.PROTECT
    )

    def __int__(self):
        return self.valor

    class Meta:
        app_label = 'app'


class Comentario(models.Model):
    texto = models.TextField(max_length=2000,)
    fechaHora = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(null=True)
    usuario = models.ForeignKey(
        User,
        related_name='comentarios',
        on_delete=models.PROTECT
    )
    pelicula = models.ForeignKey(
        Pelicula,
        related_name='comentarios',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.texto

    class Meta:
        app_label = 'app'


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app'

class PeliculaCategoria(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        related_name='peliculascategoria',
        on_delete=models.PROTECT
    )
    pelicula = models.ForeignKey(
        Pelicula,
        related_name='peliculascategoria',
        on_delete=models.PROTECT
    )
    def __int__(self):
        return self.pelicula

    class Meta:
        app_label = 'app'