from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from categorie.models import Categorie
from equipement.models import Equipement
from message.models import Message
from panne.forms import PanneForm
from panne.models import Panne
from statut.models import Statut


@login_required(login_url='inscription')
def supprimer_panne(request, pk):
    panne = Panne.objects.filter(id=pk).delete()
    context = {'panne': panne}
    return redirect('../liste')


@login_required(login_url='inscription')
def ajout_panne(request):
    form = PanneForm()
    if request.method == 'POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajoup_panne.html', context)


@login_required(login_url='inscription')
def modif_panne(request, pk):
    panne = Panne.objects.get(id=pk)
    form = PanneForm(instance=panne)
    if request.method == 'POST':
        form = PanneForm(request.POST, instance=panne)
        if form.is_valid():
            form.save()
            return redirect('../liste')
    context = {'form': form}
    return render(request, 'ajoup_panne.html', context)


@login_required(login_url='inscription')
def panne(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    f = 0
    for i in notification:
        f = f + 1
    e = 0
    for i in panne:
        e = e + 1
    # if nb != e:
    #    chain = "fa fa-play fa-rotate-90"
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'count': e, 'nb': f}
    return render(request, 'panne.html', context)

