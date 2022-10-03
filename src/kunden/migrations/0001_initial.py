# Generated by Django 4.0.2 on 2022-02-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('kundenNr', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='KundenNr')),
                ('firma', models.CharField(blank=True, max_length=30, null=True)),
                ('anschrift', models.CharField(blank=True, max_length=30, null=True)),
                ('telefon', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('letzte_Gespraeche', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
