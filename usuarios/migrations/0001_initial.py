# Generated by Django 4.1.2 on 2022-10-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('apellido_usuario', models.CharField(max_length=200)),
                ('edad_usuario', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
