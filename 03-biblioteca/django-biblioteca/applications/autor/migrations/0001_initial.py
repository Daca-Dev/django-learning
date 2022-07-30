# Generated by Django 3.2.6 on 2021-09-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellido')),
                ('nacionalidad', models.CharField(max_length=20, verbose_name='nacionalidad')),
                ('edad', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]