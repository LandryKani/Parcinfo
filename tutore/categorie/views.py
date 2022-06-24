from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from categorie.forms import CategorieForm
from categorie.models import Categorie
from equipement.models import Equipement
from message.models import Message
from panne.models import Panne
from statut.models import Statut


@login_required(login_url='inscription')
def modif_categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    form = CategorieForm(instance=categorie)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajout_cat.html', context)


@login_required(login_url='inscription')
def ajout_categorie(request):
    form = CategorieForm()
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajout_cat.html', context)

@login_required(login_url='inscription')
def supprimer_ca(request, pk):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.filter(id=pk).delete()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    e = 0
    f = 0
    for i in categorie:
        e = e + 1
    for i in notification:
        f = f + 1
    nb = e
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'count': e, 'nb': f}
    return redirect('../liste')



@login_required(login_url='inscription')
def categorie(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    chain = "fa fa-play fa-rotate-270"
    e = 0
    for i in categorie:
        e = e + 1
    nb = e
    #if nb != e:
    #    chain = "fa fa-play fa-rotate-90"
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'count': e, 'nb': nb}
    return render(request, 'categorie.html', context)


