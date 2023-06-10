from django.shortcuts import render,redirect
from django.views import generic
from .models import *
from django.db.models import Count
from .forms import ConsomationForm, JourForm, AlimentForm, ProblemeForm
from .formp import PersonneForm
from django.db.models import Max

# Create your views here.

def index(request):
    nb_Personne= Personne.objects.all().count()
    nb_Aliment=Aliment.objects.all().count()
    nb_Consommation=Consomation.objects.all().count()
    select_pers=Personne.objects.get(nom='gerazayis')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits':num_visits,
        'nom': select_pers,
        'Total_Personne': nb_Personne,
        'Total_Aliment': nb_Aliment,
        'Total_conso': nb_Consommation,
    }
    return render(request,'index.html',context=context)

def inscription(request):
    return render(request, 'inscription.html')

def connexion(request):
    return render(request,'connexion.html')


def prerepas(request):
    personne = Personne.objects.get(id=1)
    consommations = Consomation.objects.filter(Nom_Personne=personne)

    context = {'personne': personne, 'consommations': consommations}
    return render(request, 'prerepas.html', context)

def premaladie(request):
    personne = Personne.objects.get(id=1)
    consommations = Consomation.objects.filter(Nom_Personne=personne)

    context = {'personne': personne, 'consommations': consommations}
    return render(request, 'premaladie.html', context)

def ajouter(request):
    if request.method == 'POST':
        personne_form = PersonneForm(request.POST)
        consommation_form = ConsomationForm(request.POST)
        if (personne_form.is_valid()):
            consommation = consommation_form.save(commit=True)
            consommation.save()
    else:
        #personne_form = PersonneForm()
        consommation_form = ConsomationForm()
    context = {'consommation_form': consommation_form}
    return render(request, 'formulaire.html', context)

def repasrec(request):
    personne = Personne.objects.get(id=3)
    jours = Jour.objects.values('id_jour').distinct()
    repas_consommes = []
    for jour in jours:
        repas = Jour.objects.filter(Nom_Personne_id=3,id_jour=jour['id_jour']).values('repas__nom').annotate(quantite=Max('repas')).order_by('-quantite').first()
        repas_consommes.append({'jour': jour['id_jour'], 'repas': repas})
    context = {'repas_consommes': repas_consommes,
               'personne':personne}
    return render(request, 'repasrec.html', context)

def listrepas(request):
    personne = Personne.objects.get(id=3)
    aliment = Aliment.objects.all()
    consommationsr = Consomation.objects.filter(Nom_Personne=personne)

    context = {'personne': personne, 'aliment': aliment, 'consomation':consommationsr}
    return render(request, 'listrepas.html', context)