from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('index', views.index, name='index'),
    path('connexion',views.connexion, name='connexion'),
    path('prerepas', views.prerepas,name='prerepas'),
    path('premaladie', views.premaladie,name='premaladie'),
    path('formulaire', views.ajouter, name='ajouter'),
    path('repasrec', views.repasrec, name='repasrec'),
    path('listrepas', views.listrepas, name='listrepas'),
]