from django.urls import path, include
from . import views

urlpatterns=[
    path('ajouter/', views.ajout_panne, name='ajouterPA'),
    path('modifier/<str:pk>', views.modif_panne, name='modifierPA'),
    path('supprimer/<str:pk>', views.supprimer_panne, name='supprimerPA'),
    path('liste/', views.panne, name='listeP'),
]