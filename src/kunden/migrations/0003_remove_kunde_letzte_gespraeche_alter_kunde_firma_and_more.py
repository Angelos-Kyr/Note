# Generated by Django 4.0.2 on 2022-05-12 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kunden', '0002_kunde_stadt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kunde',
            name='letzte_Gespraeche',
        ),
        migrations.AlterField(
            model_name='kunde',
            name='firma',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Verkmerk',
            fields=[
                ('gespraechs_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='GesprächsNr')),
                ('datum_des_Gespraechs', models.DateTimeField(auto_now=True)),
                ('gesclecht', models.CharField(blank=True, choices=[('Frau', 'Frau'), ('Herrn', 'Herrn')], default='', max_length=50, null=True)),
                ('mitarbeiter', models.CharField(default='', max_length=400, verbose_name='Mitarbeiter Name')),
                ('betreff', models.CharField(default='', max_length=100, null=True)),
                ('inhalt_des_gesprächs', models.CharField(blank=True, choices=[('Ruft wieder an', 'Ruft wieder an'), ('Wünscht Rückruf', 'Wünscht Rückruf'), ('Wünscht Termin', 'Wunscht Termin'), ('Anderes Thema', 'Anderes Thema')], default='', max_length=50, null=True)),
                ('kommentare', models.TextField(blank=True, default='', max_length=4000, null=True)),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kunden.kunde')),
            ],
        ),
    ]