from django.urls import path
from . import views

urlpatterns = [

    path('', views.connexionPage, name='connexion'),
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('logout/', views.logoutUser, name="logout"),

]
