# Generated by Django 4.2 on 2023-06-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final', '0004_delete_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='kilometros',
            field=models.CharField(max_length=3),
        ),
    ]
