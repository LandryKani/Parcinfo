from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from categorie.models import Categorie
from equipement.forms import EquipementForm
from equipement.models import Equipement
from message.models import Message
from panne.models import Panne
from statut.models import Statut


@login_required(login_url='connexionPage')
def equipement(request, pk):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    e = 0
    for i in notification:
        e = e + 1
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie,
               'notification': notification, 'nb': e}
    return render(request, 'home.html', context)


@login_required(login_url='base')
def equipementG(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    e = 0
    for i in equipement:
        e = e + 1
    nb = e
    f = 0
    for i in notification:
        f = f + 1
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'count': e, 'nb': f}
    return render(request, 'equipement.html', context)


@login_required(login_url='inscription')
def liste_equipement(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie}
    return render(request, 'liste_equipement.html', context)


@login_required(login_url='inscription')
def ajout_eq(request):
    form = EquipementForm()
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajout_eq.html', context)


@login_required(login_url='inscription')
def modif_eq(request, pk):
    equipement = Equipement.objects.get(id=pk)
    form = EquipementForm(instance=equipement)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('../listeE')
    context = {'form': form}
    return render(request, 'ajout_eq.html', context)


@login_required(login_url='inscription')
def supprimer_eq(request, pk):
    equipement = Equipement.objects.filter(id=pk).delete()
    context = {'equipement': equipement}
    return redirect('../liste')