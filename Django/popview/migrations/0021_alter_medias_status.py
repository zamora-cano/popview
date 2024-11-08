# Generated by Django 4.2.16 on 2024-10-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popview', '0020_alter_capitulos_status_alter_cuentas_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medias',
            name='status',
            field=models.CharField(choices=[('accion', 'Acción'), ('comedia', 'Comedia'), ('drama', 'Drama'), ('terror', 'Terror'), ('ciencia_ficcion', 'Ciencia Ficción'), ('romance', 'Romance'), ('aventura', 'Aventura'), ('documental', 'Documental'), ('fantasia', 'Fantasía'), ('animacion', 'Animación'), ('musical', 'Musical'), ('thriller', 'Thriller'), ('misterio', 'Misterio'), ('biografico', 'Biográfico'), ('ficcion_historica', 'Ficción Histórica'), ('guerra', 'Guerra'), ('western', 'Western'), ('superheroes', 'Superhéroes'), ('deportes', 'Deportes'), ('familia', 'Familia'), ('ciencia', 'Ciencia'), ('ficcion_juvenil', 'Ficción Juvenil'), ('romcom', 'Romántica-Comedia'), ('zombies', 'Zombies'), ('post_apocaliptico', 'Post-apocalíptico'), ('danza', 'Danza'), ('arte', 'Arte'), ('reality', 'Reality'), ('viajes', 'Viajes')], default='nuevo', max_length=25),
        ),
    ]
