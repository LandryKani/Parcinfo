from django.urls import path, include
from . import views

urlpatterns = [
    path('ajouter/', views.ajout_categorie, name='ajouterCA'),
    path('modifier/<str:pk>', views.modif_categorie, name='modifierCA'),
    path('supprimer/<str:pk>', views.supprimer_ca, name='supprimerCA'),
    path('liste/', views.categorie, name='listeCA')
]