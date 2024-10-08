# Generated by Django 5.1.1 on 2024-09-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='email',
            field=models.EmailField(default='non', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='ninguna', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='segundo_apellido',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='alumno',
            name='segundo_nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='docente',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='ninguno', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docente',
            name='segundo_apellido',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='docente',
            name='segundo_nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
