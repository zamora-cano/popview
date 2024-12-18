# Generated by Django 4.2.16 on 2024-10-09 01:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Capitulos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('numero_capitulo', models.SmallIntegerField(verbose_name='Número de capítulo')),
                ('temporada', models.SmallIntegerField(verbose_name='Temporada')),
                ('ibm', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='IBM')),
                ('intro_start', models.PositiveSmallIntegerField(verbose_name='Intro Start')),
                ('intro_end', models.PositiveSmallIntegerField(verbose_name='Intro End')),
                ('end', models.SmallIntegerField(verbose_name='End')),
            ],
        ),
        migrations.CreateModel(
            name='Covers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('perfil', models.BooleanField(verbose_name='Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Medias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('serie', models.BooleanField(default=False, verbose_name='Serie')),
                ('infantil', models.BooleanField(default=False, verbose_name='Infantil')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias_banner', to='popview.banners', verbose_name='Banner')),
                ('cover', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias_cover', to='popview.covers', verbose_name='Cover')),
            ],
        ),
        migrations.CreateModel(
            name='Posters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
                ('infantil', models.BooleanField(default=False, verbose_name='Infantil')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='popview.cuentas', verbose_name='Cuenta')),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='popview.imagenes', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Vistas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('segundo', models.PositiveSmallIntegerField(verbose_name='Segundo')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vistas_media', to='popview.medias', verbose_name='Media')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vistas_usuario', to='popview.usuarios', verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos_capitulo', to='popview.capitulos', verbose_name='Capítulo')),
            ],
        ),
        migrations.AddField(
            model_name='medias',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias_poster', to='popview.posters', verbose_name='Poster'),
        ),
        migrations.CreateModel(
            name='Media_has_genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='generos_media', to='popview.generos', verbose_name='Género')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='media_generos', to='popview.medias', verbose_name='Media')),
            ],
        ),
        migrations.AddField(
            model_name='generos',
            name='imagen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generos', to='popview.imagenes', verbose_name='Imagen'),
        ),
        migrations.CreateModel(
            name='Deseos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deseo_media', to='popview.medias', verbose_name='Media')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deseo_usuario', to='popview.usuarios', verbose_name='Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='capitulos',
            name='cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='capitulos_cover', to='popview.covers', verbose_name='Cover'),
        ),
        migrations.AddField(
            model_name='capitulos',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos_media', to='popview.medias', verbose_name='Media'),
        ),
    ]
