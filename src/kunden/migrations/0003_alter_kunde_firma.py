# Generated by Django 4.0.2 on 2022-03-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunden', '0002_kunde_stadt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunde',
            name='firma',
            field=models.CharField(max_length=30, null=True),
        ),
    ]