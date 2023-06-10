import psycopg2
from django.db import models

class AlimentDAO:
    def __init__(self):
        # Connexion à la base de données
        self.conn = psycopg2.connect(host="localhost", database="nutrition", user="gerazayis", password="123Gerazayis?")

    # Ajouter un Aliment
    def ajouter_Aliment(self, Aliment):
        cursor = self.conn.cursor()
        sql = "INSERT INTO Aliment (nom, calories, type) VALUES (%s, %s, %s)"
        values = (Aliment.nom, Aliment.calories, Aliment.type)
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    # Obtenir un Aliment par son identifiant
    def get_Aliment_by_id(self, id_Aliment):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Aliment WHERE id_Aliment = %s"
        values = (id_Aliment,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result:
            Aliment = Aliment(result[1], result[2], result[3])
            Aliment.id = result[0]
        else:
            Aliment = None
        cursor.close()
        return Aliment

    # Obtenir tous les Aliments
    def get_all_Aliments(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM Aliment"
        cursor.execute(sql)
        results = cursor.fetchall()
        Aliments = []
        for result in results:
            Aliment = Aliment(result[1], result[2], result[3])
            Aliment.id = result[0]
            Aliments.append(Aliment)
        cursor.close()
        return Aliments

    # Mettre à jour unAliment
    def update_Aliment(self, Aliment):
        cursor = self.conn.cursor()
        sql = "UPDATE Aliment SET nom = %s, calories = %s, type = %s WHERE id_Aliment = %s"
        values = (Aliment.nom, Aliment.calories, Aliment.type, Aliment.id)
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    # Supprimer un Aliment
    def delete_Aliment(self, id_Aliment):
        cursor = self.conn.cursor()
        sql = "DELETE FROM Aliment WHERE id_Aliment = %s"
        values = (id_Aliment,)
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

class PersonneDAO:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", database="nutrition", user="gerazayis", password="123Gerazayis?")

    def AjoutPersonne(self, Personne):
        nom=Personne.nom
