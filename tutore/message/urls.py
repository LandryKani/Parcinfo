from django.urls import path, include
from . import views

urlpatterns = [
            path('ajouter/', views.creer_notification, name='ajouterNO'),
            path('ajouter/<str:pk>', views.compose_Mail, name='ajouterNOuser'),
            path('liste/', views.liste_notification, name='listeNO'),
            path('liste/envoyer/', views.mail_envoye, name='listeNOenvoye'),
            path('detail/Notification/<str:pk>', views.detail_notification, name='detail_notification'),
            path('markread/<str:pk>', views.markasread, name='markasread')
]
