from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreerUtilisateur


# Create your views here.
def inscriptionPage(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if User.objects.filter(username=username):
            messages.error(request, "Nom utilisateur exist déja! Essayer autre chose")
            return redirect('inscription')
        if User.objects.filter(email=email):
            messages.error(request, "Email déja existant!")
            return redirect('inscription')
        if len(username) > 15:
            messages.error(request, "Nom utilisateur doit etre sous 10 caracter")
        if pass1 != pass2:
            messages.error(request, "Mot de passe ne match pas")
        if not username.isalnum():
            messages.error(request, "Non Utilisateur doit etre alphanumerique")
            return redirect('inscription')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.Nom_utilisateur = username
        myuser.save()
        messages.success(request, "Votre compte a etait correctement Crée")
        # Welcome Email
        subject = "Welcome to TECH GROUP"
        message = "Hello" + myuser.Nom_utilisateur + "!! \n" + "Welcome to TECH GROUP!! \n Merci de visiter notre site web \n Nous vous avons envoyer une email de confirmation, s'il vous plait veillez confirmer votre adresse pour activer votre compte. \n\n Merci"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('connexion')

    return render(request, 'inscription.html')


def connexionPage(request):
    if request.user.is_authenticated:
        return redirect('base')
    else:
        if request.method == 'POST':
            username = request.POST.get('nomutil')
            password = request.POST.get('pass1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'connexion.html', context)


def logoutUser(request):
    logout(request)
    return redirect('connexion')
