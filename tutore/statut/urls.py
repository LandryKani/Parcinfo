from django.urls import path, include
from . import views

urlpatterns = [
    path('ajouter/', views.ajout_statut, name='ajouterST'),
    path('modifier/<str:pk>', views.modif_statut, name='modifierST'),
    path('supprimer/<str:pk>', views.statut, name='supprimerST'),
    path('liste/', views.statut, name='listeST'),
]