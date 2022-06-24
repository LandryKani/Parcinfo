from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from categorie.models import Categorie
from equipement.models import Equipement
from panne.models import Panne
from statut.forms import StatutForm
from statut.models import Statut


@login_required(login_url='inscription')
def ajout_statut(request):
    form = StatutForm()
    if request.method == 'POST':
        form = StatutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajout_statut.html', context)


@login_required(login_url='inscription')
def modif_statut(request, pk):
    statut = Statut.objects.get(id=pk)
    form = StatutForm(instance=statut)
    if request.method == 'POST':
        form = StatutForm(request.POST, instance=statut)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajout_statut.html', context)


@login_required(login_url='inscription')
def statut(request, pk):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie}
    return render(request, 'statut.html', context)


@login_required(login_url='inscription')
def statut(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    chain = "fa fa-play fa-rotate-270"
    e = 0
    for i in statut:
        e = e + 1
    nb = e
    #if nb != e:
    #    chain = "fa fa-play fa-rotate-90"
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'count': e, 'nb': nb}
    return render(request, 'statut.html', context)
