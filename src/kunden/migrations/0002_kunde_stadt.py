# Generated by Django 4.0.2 on 2022-02-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kunde',
            name='stadt',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
