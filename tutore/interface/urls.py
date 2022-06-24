from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('compte.urls')),
    path('equipement/', include('equipement.urls')),
    path('panne/', include('panne.urls')),
    path('statut/', include('statut.urls')),
    path('categorie/', include('categorie.urls')),
    path('notification/', include('message.urls')),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
    path('home/', views.home, name='base'),
    path('base1/', views.base1, name='base1'),
    #path('aboutus/', views.acceuil, name='acceuil'),
]
