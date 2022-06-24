from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.core.mail import send_mail, send_mass_mail
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from interface.forms import CreerUtilisateur
from equipement.models import Equipement
from message.models import Message
from panne.models import Panne
from statut.models import Statut
from categorie.models import Categorie
from equipement.forms import EquipementForm
from panne.forms import PanneForm
from statut.forms import StatutForm
from categorie.forms import CategorieForm

# Create your views here.


def base1(request):
    return render(request, 'base1.html')


def test(request):
    return render(request, 'test.html')


def home(request):
    equipement = Equipement.objects.all()
    nbE = Equipement.objects.count()
    panne = Panne.objects.all()
    nbP = Panne.objects.count()
    statut = Statut.objects.all()
    nbS = Statut.objects.count()
    categorie = Categorie.objects.all()
    nbC = Categorie.objects.count()
    notification = Message.objects.all()
    leuser = request.user
    lesuser = User.objects.all()
    e = 0
    f = 0
    unread = []
    for i in notification:
        if i.statut == "unread":
            if e < 2:
                unread.append(i)
            e = e + 1
        f = f + 1
    context = {'lesuser': lesuser, 'nbE': nbE, 'nbP': nbP, 'nbC': nbC, 'nbS': nbS, 'user': leuser, 'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'unread': unread, 'nb':e,'ndnotif': f}
    return render(request, 'home.html', context)


@login_required(login_url='connexionPage')
def base2(request):
    equipement = Equipement.objects.all()
    nbE = 0
    for i in equipement:
        nbE = nbE + 1
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    notification = Message.objects.all()
    leuser = request.user
    lesuser = User.objects.all()
    e = 0
    f = 0
    unread = []
    for i in notification:
        if i.statut == "unread":
            if e < 2:
                unread.append(i)
            e = e + 1
        f = f + 1
    context = {'user': leuser, 'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie,
               'unread': unread, 'nb': e, 'ndnotif': f, 'nbE': nbE, 'lesuser': lesuser}
    return render(request, 'home.html', context)


@login_required(login_url='connexionPage')
def base(request):
    equipement = Equipement.objects.all()
    nbE = Equipement.objects.count()
    panne = Panne.objects.all()
    statut = Statut.objects.all()
    categorie = Categorie.objects.all()
    context = {'equipement': equipement, 'panne': panne, 'statut': statut, 'categorie': categorie, 'nbE':nbE}
    return render(request, 'base.html', context)


class SendFormEmail(View):

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        send_mail(
            'Subject - Django Email Testing',
            'Hello ' + name + ',\n' + message,
            'sender@example.com',  # Admin
            [
                email,
            ]
        )

        send_mail(
            'subject',
            'body of the message',
            'sender@example.com',
            [
                'yveszogo960@gmail.com',
                'fotsochrist1@gmail.com'
            ]
        )

        message1 = (
        'Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
        message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
        send_mass_mail((message1, message2), fail_silently=False)

        # Redirect to same page after form submit
        messages.success(request, ('Message envoyé.'))
        return redirect('base')
