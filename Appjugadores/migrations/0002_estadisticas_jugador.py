# Generated by Django 4.0.4 on 2022-07-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appjugadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadisticas',
            name='jugador',
            field=models.CharField(default='', max_length=50),
        ),
    ]
