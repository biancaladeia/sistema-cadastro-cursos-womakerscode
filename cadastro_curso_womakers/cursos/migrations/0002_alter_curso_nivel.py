# Generated by Django 4.2.6 on 2023-10-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')], max_length=50),
        ),
    ]
