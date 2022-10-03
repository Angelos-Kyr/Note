from django import forms
from .models import Kunde, Verkmerk

class KundeCreateForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = ['kundenNr', 'firma','email', 'anschrift','stadt', 'telefon', 'fax']

    def clean_firma(self):
        firma = self.cleaned_data.get('firma')
        if not firma:
            raise forms.ValidationError('This field is required')
        for instance in Kunde.objects.all():
            if instance.firma == firma:
                raise forms.ValidationError(firma + 'is already created')
        return firma




class KundenSearchForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = ['firma']

class KundeUpdateForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = ['email', 'anschrift','stadt', 'telefon', 'fax']


class VerkmerkForm(forms.ModelForm):
    class Meta:
        model = Verkmerk
        fields= ['gespraechs_id', 'firma', 'gesclecht', 'mitarbeiter', 'betreff', 'inhalt_des_gesprächs','comments']

class GespreachSearchForm(forms.ModelForm):
    class Meta:
        model = Verkmerk
        fields = ['firma']

class Show_commentsForm(forms.ModelForm):
    class Meta:
        model = Verkmerk
        fields = ['comments']