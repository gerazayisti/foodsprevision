from django.db import models
from django.urls import reverse
import psycopg2

#creation de nos modeles

class Consomation(models.Model):
    id=models.AutoField
    Nom_Personne=models.ForeignKey('Personne',on_delete=models.SET_NULL,null=True)
    quantite=models.IntegerField(help_text='preciser la quantite en entier')
    id_jour=models.ForeignKey('Jour', on_delete=models.RESTRICT)
    id_aliments=models.ForeignKey('Aliment',on_delete=models.RESTRICT)
    id_probleme=models.ForeignKey('Probleme',on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.Nom_Personne}'
    
    def get_absolute_url(self):
        return reverse('detail-Consomation',args=[str(self.id)])
    
    

class Jour(models.Model):
    id=models.AutoField
    Nom_Personne=models.ForeignKey('Personne',on_delete=models.SET_NULL,null=True)
    jour=(('Lundi','1'),('Mardi','2'),('Mercredi','3'),('Jeudi','4'),('Vendredi','5'),('Samedi','6'),('Dimanche','7'))
    id_jour=models.CharField(max_length=11,choices=jour,default='Lundi',help_text='identifiant du jour')
    repas=models.ForeignKey('Aliment', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.id_jour}'
    
class Probleme(models.Model):
    nom=models.CharField(max_length=70,help_text='nom du probleme de sante')
    symptome=models.CharField(max_length=70,help_text='nom du symptomes')
    level=(('1','null'),('2','faibles'),('3','moyen'),('4','graves'),('5','tres graves'))
    gravite=models.CharField(max_length=10,choices=level,default=1,help_text='niveau de gravite de 1 a 5')

    def __str__(self):
        return f'{self.nom}: gravite ={self.gravite}'
    
class Aliment(models.Model):
    nom=models.CharField(max_length=70,help_text='nom du repas')
    calorie=models.IntegerField(help_text='nobre de calorie')
    probleme=models.ManyToManyField(Probleme, blank=True)
    types=(('1','Fruit'),('2','Legume'),('3','Viande'),('4','Poisson'),('5','autre'))
    type_Aliment=models.CharField(max_length=10,choices=types,default='autres',help_text='le type d\'aliment consommes')

    def __str__(self):
        return self.nom


class Personne(models.Model):
    id=models.AutoField
    nom=models.CharField(max_length=200,help_text='votre nom svp')
    age=models.PositiveIntegerField(help_text='votre age ici')
    sexe=models.CharField(max_length=10,help_text='votre sexe')
    taille=models.IntegerField(help_text='votre taille svp en cm (exemple:145)')
    poids=models.IntegerField(help_text='votre poids actuel')
    def __str__(self):
        return f'{self.nom}'
    
    def get_absolute_url(self):
        return reverse('detail-Personne',args=[str(self.nom)])

#----------------------->>> class DAO <<<-----------------------
class AlimentDAO:
    # Ajouter un aliment
    def ajouter_aliment(self, aliment):
        Aliment.objects.create(
            nom=aliment.nom, 
            calories=aliment.calories, 
            type=aliment.type, 
            description=aliment.description
        )

    # Obtenir un aliment par son identifiant
    def get_aliment_by_id(self, id_aliment):
        try:
            aliment = Aliment.objects.get(id=id_aliment)
        except Aliment.DoesNotExist:
            aliment = None
        return aliment

    # Obtenir tous les aliments
    def get_all_aliments(self):
        return Aliment.objects.all()

    # Mettre à jour un aliment
    def update_aliment(self, aliment):
        aliment_upd = Aliment.objects.get(id=aliment.id)
        aliment_upd.nom = aliment.nom
        aliment_upd.calories = aliment.calories
        aliment_upd.type = aliment.type
        aliment_upd.description = aliment.description
        aliment_upd.save()

    # Supprimer un aliment
    def delete_aliment(self, id_aliment):
        Aliment.objects.filter(id=id_aliment).delete()