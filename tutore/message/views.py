from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from categorie.models import Categorie
from equipement.models import Equipement
from message.forms import MessageForm
from message.models import Message
from panne.models import Panne
from statut.models import Statut


@login_required(login_url='inscription')
def creer_notification(request):
    lesuser = User.objects.all()
    dest = ""
    response = " "
    e = 0  # destinateur counter
    d = 0  # expediteur counter
    form = Message()
    context = {'response': response, 'form': form, 'lesuser': lesuser, 'destinateur': dest}
    if request.method == 'POST':
        destinataire = request.POST['destinateur']
        expediteur = request.user.username
        text = request.POST['text']
        user = User.objects.all()
        for i in user:
            if i.username == destinataire:
                d = 1
        if d == 1:
            form.expediteur = expediteur
            form.destinataire = destinataire
            form.text = text
            form.save()
        else:
            response = " error : Please enter valid values !!!"
            context = {'response': response, 'form': form, 'lesuser': lesuser}
            return redirect('../listeNO')
    return render(request, 'ajout_notif.html', context)


@login_required(login_url='inscription')
def compose_Mail(request, pk):
    lesuser = User.objects.all()
    message = Message.objects.get(id=pk)
    utilisateur = User.objects.all()
    for l in utilisateur:
        if l.username == message.expediteur:
            dest = User.objects.get(id=l.id)
    response = " "
    e = 0  # destinateur counter
    d = 0  # expediteur counter
    form = Message()
    context = {'response': response, 'form': form, 'lesuser': lesuser, 'destinateur': dest.username}
    if request.method == 'POST':
        destinataire = request.POST['destinateur']
        expediteur = request.user.username
        text = request.POST['text']
        user = User.objects.all()
        for i in user:
            if i.username == destinataire:
                d = 1
        if d == 1:
            form.expediteur = expediteur
            form.destinataire = destinataire
            form.text = text
            form.save()
        else:
            response = " error : Please enter valid values !!!"
            context = {'response': response, 'form': form, 'lesuser': lesuser, 'destinateur': dest}
            return redirect('ajouterNO', context)
    return render(request, 'ajout_notif.html', context)


@login_required(login_url='inscription')
def liste_notification(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    message = Message.objects.all()
    leuser = request.user
    lesuser = User.objects.all()
    e = 0
    j = 0
    notifications = []
    for i in message:
        e = e + 1
        if i.destinataire == leuser.username:
            notifications.append(i)
            j = j + 1
    list_expediteur = []
    list_expediteur.append("admin")
    for i in notifications:
        ct = 0
        for k in list_expediteur:
            if k == i.expediteur:
                ct = 1
        if ct == 0:
            list_expediteur.append(i.expediteur)

    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie,
               'notifications': notifications, 'nb': j, 'liste_nom': list_expediteur, 'lesuser': lesuser}
    return render(request, 'notification.html', context)


@login_required(login_url='inscription')
def mail_envoye(request):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    message = Message.objects.all()
    leuser = request.user
    lesuser = User.objects.all()
    e = 0
    j = 0
    notification = []
    notification = Message.objects.filter(expediteur=leuser.username)
    list_destinateur = []
    for i in notification:
        ct = 0
        for k in list_destinateur:
            if k == i.destinataire:
                ct = 1
        if ct == 1:
            list_destinateur.append(i.destinataire)
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie,
               'notification': notification, 'nb': j, 'liste_nom': list_destinateur, 'lesuser': lesuser}
    return render(request, 'mailenvoye.html', context)


@login_required(login_url='inscription')
def detail_notification(request, pk):
    messages = Message.objects.all()
    message = Message.objects.get(id=pk)
    user = User.objects.filter(username=message.expediteur)
    leuser = request.user
    lesuser = User.objects.all()
    e = 0
    j = 0
    notification = []
    for i in messages:
        e = e + 1
        if i.destinataire == leuser.username:
            notification.append(i)
            j = j + 1
    context = {'notification': notification, 'nb': j, 'sms': message, 'user': user, 'lesuser':lesuser, 'key':pk}
    return render(request, 'detail_notification.html', context)


@login_required(login_url='inscription')
def markasread(request, pk):
    equipement = Equipement.objects.all()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    notif = Message.objects.filter(id=pk).update(statut="Read")
    #form = MessageForm(request.POST, instance=notif)
    e = "ok!!"
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie,
               'notification': notification, 'mot': e, 'form':pk}
    #ky = pk
    #for i in notification:
    #    e = "bonjour"
    #    if i.id == ky:
    #        e = "there is a key!!"
    #    else:
    #        i.statut = "read"
    #        i.save()
    #        return redirect('../liste', context)
    return redirect('../liste', context)
