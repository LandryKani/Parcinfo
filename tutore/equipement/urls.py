from django.urls import path, include
from . import views

urlpatterns = [
            path('ajouter/', views.ajout_eq, name='ajouterE'),
            path('mofdifier/<str:pk>', views.modif_eq, name='modifierE'),
            path('supprimer/<str:pk>', views.supprimer_eq, name='supprimerE'),
            path('liste/', views.equipementG, name='listeE'),
            #path('liste_equipement/', views.liste_equipement, name='liste'),
            # path('modifier/<str:pk>', views.equipement, name='equipement'),
]