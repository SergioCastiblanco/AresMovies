# Generated by Django 3.0.5 on 2020-05-16 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='calificaciones', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comentarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
