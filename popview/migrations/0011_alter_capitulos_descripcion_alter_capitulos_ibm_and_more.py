# Generated by Django 4.2.16 on 2024-10-09 03:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popview', '0010_alter_capitulos_descripcion_alter_capitulos_ibm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulos',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='ibm',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='IBM'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='intro_end',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Intro End'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='intro_start',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Intro Start'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='numero_capitulo',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Número de capítulo'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='temporada',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Temporada'),
        ),
    ]
