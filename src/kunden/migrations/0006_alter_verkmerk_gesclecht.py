    # Generated by Django 4.0.2 on 2022-05-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunden', '0005_remove_kunde_letzte_gespraeche_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verkmerk',
            name='gesclecht',
            field=models.CharField(blank=True, choices=[('Frau', 'Frau'), ('Herrn', 'Herrn')], default='', max_length=50, null=True),
        ),
    ]
