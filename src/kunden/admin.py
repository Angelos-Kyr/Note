from django.contrib import admin
from .forms import *
from .models import Kunde

# Register your models here.
class KundeCreateAdmin(admin.ModelAdmin):
    list_display = ['kundenNr','firma','email']
    form = KundeCreateForm
    list_filter = ['firma']
    search_fields = ['firma', 'kundeNr']

admin.site.register(Kunde, KundeCreateAdmin)

