# Generated by Django 4.0.4 on 2022-05-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(blank=True, max_length=200, null=True)),
                ('p_academico', models.CharField(max_length=100)),
            ],
        ),
    ]