from django import forms
from .models import Consomation, Jour, Aliment, Probleme



class ConsomationForm(forms.ModelForm):
    class Meta:
        model = Consomation
        fields = ['Nom_Personne', 'quantite', 'id_jour', 'id_aliments', 'id_probleme']

class JourForm(forms.ModelForm):
    class Meta:
        model = Jour
        fields = ['id_jour', 'repas']

class AlimentForm(forms.ModelForm):
    class Meta:
        model = Aliment
        fields = ['nom', 'calorie', 'type_Aliment']

class ProblemeForm(forms.ModelForm):
    class Meta:
        model = Probleme
        fields = ['nom', 'symptome', 'gravite']