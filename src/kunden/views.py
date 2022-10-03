from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import KundeCreateForm, KundenSearchForm, KundeUpdateForm, VerkmerkForm, GespreachSearchForm, Show_commentsForm
#from gespraechsvermerk.forms import VerkmerkForm




# Create your views here.
def home(request):
    title='Welcome: this is the home page'
    context={
        "title":title,
    }
    return render(request, "kundenlist.html", context)


def list_kunde(request):
    title='Kundenliste'
    form = KundenSearchForm(request.POST or None)
    queryset = Kunde.objects.all()
    context={
        "title":title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Kunde.objects.filter(firma__icontains=form['firma'].value())
        context = {
            "forms": form,
            "title": title,
            "queryset": queryset,

        }
    return render(request, "kundelist.html", context)


def add_kunde(request):
    form = KundeCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Erfolgreich gespeichert')
        return redirect('/kundelist/')
    context = {
        "form":form,
        "title": "Add Kunde",
    }
    return render(request, "add_kunde.html", context)

def update_kundenlists(request, pk):
    queryset = Kunde.objects.get(kundenNr=pk)
    form = KundeUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = KundeUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Erfolgreich gespeichert')
            return redirect('/kundelist')
    context = {
        'form': form
    }
    return render(request, 'add_kunde.html', context)

def delete_kunde(request, pk):
    queryset = Kunde.objects.get(kundenNr=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Erfolgreich löschen')
        return redirect('/kundelist')
    return render(request, 'delete_kunde.html')


def add_notiz(request):
    form = VerkmerkForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Erfolgreich gespeichert')
        return redirect('/gespreachsverlauf/')
    context = {
        "form":form,
        "title": "Gespächsvermerk",
    }
    return render(request, "add_notiz.html", context)

def gespreachsverlauf(request):
    title='Gesprächsverlauf'
    form = GespreachSearchForm(request.POST or None)
    queryset = Verkmerk.objects.all()
    context={
        "title":title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Verkmerk.objects.filter(firma=form['firma'].value())
        context = {
            "forms": form,
            "title": title,
            "queryset": queryset,

        }
    return render(request, "gespreachsverlauf.html", context)

def delete_verlauf(request, pk):
    queryset = Verkmerk.objects.get(gespraechs_id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Erfolgreich löschen')
        return redirect('/gespreachsverlauf/')
    return render(request, 'delete_verlauf.html')


def show_comments(request, pk):
    queryset = Verkmerk.objects.get(gespraechs_id=pk)
    form = Show_commentsForm(instance=queryset)
    if request.method == 'POST':
        form = Show_commentsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Erfolgreich gespeichert')
            return redirect('/show_comments')
    context = {
        'form': form,
        'title': 'Kommentare',
    }
    return render(request, 'show_kom.html', context)