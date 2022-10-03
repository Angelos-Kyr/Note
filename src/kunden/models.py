from django.db import models

# Create your models here.
class Kunde(models.Model):
    kundenNr = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='KundenNr')
    firma = models.CharField(max_length=30, blank=False, null=True)
    anschrift = models.CharField(max_length=30, blank=True, null=True)
    stadt = models.CharField(max_length=30, blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)



    def __str__(self):
        return self.firma

class Verkmerk(models.Model):
    firma = models.ForeignKey(Kunde,on_delete=models.CASCADE)
    gespraechs_id =models.AutoField(auto_created=True, primary_key=True, serialize=False,blank=True,  verbose_name='GesprächsNr')
    datum_des_Gespraechs = models.DateTimeField(auto_now_add=False, auto_now=True)
    invoice_type= (('Frau', 'Frau'), ('Herrn', 'Herrn'),)
    gesclecht = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type)
    mitarbeiter = models.CharField('Mitarbeiter Name', max_length=400, default='', blank=False)
    betreff = models.CharField(max_length=100, default='', blank=False, null=True)
    inhalt_des_gesprächs = (
        ('Ruft wieder an', 'Ruft wieder an'),
        ('Wünscht Rückruf', 'Wünscht Rückruf'),
        ('Wünscht Termin', 'Wunscht Termin'),
        ('Anderes Thema', 'Anderes Thema'),
    )
    inhalt_des_gesprächs = models.CharField(max_length=50, default='', blank=True, null=True, choices=inhalt_des_gesprächs)
    comments = models.TextField(max_length=4000, default='', blank=True, null=True)

    def __str__(self):
        return str(self.gespraechs_id)