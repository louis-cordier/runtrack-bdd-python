import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Zoo:
    def __init__(self):
        try:
            # Connexion à la base de données
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print('Connexion à la base de données réussie')
                self.create_tables()
        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
    
    def create_tables(self):
        # Créer d'abord la table cage
        create_cage_table = """
        CREATE TABLE IF NOT EXISTS cage (
            id INT AUTO_INCREMENT PRIMARY KEY,
            superficie INT,
            capacite_max INT
        );
        """
        self.cursor.execute(create_cage_table)

        # Créer ensuite la table animal
        create_animal_table = """
        CREATE TABLE IF NOT EXISTS animal (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            race VARCHAR(255),
            id_cage INT,
            date_naissance DATE,
            pays_origine VARCHAR(255),
            FOREIGN KEY (id_cage) REFERENCES cage(id) ON DELETE SET NULL
        );
        """
        self.cursor.execute(create_animal_table)
        self.conn.commit()

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = """
        INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Animal {nom} ajouté avec succès")

    def remove_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        self.conn.commit()
        print(f"Animal avec ID {animal_id} supprimé avec succès")

    def update_animal(self, animal_id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        query = "UPDATE animal SET "
        values = []
        if nom:
            query += "nom = %s, "
            values.append(nom)
        if race:
            query += "race = %s, "
            values.append(race)
        if id_cage:
            query += "id_cage = %s, "
            values.append(id_cage)
        if date_naissance:
            query += "date_naissance = %s, "
            values.append(date_naissance)
        if pays_origine:
            query += "pays_origine = %s, "
            values.append(pays_origine)

        # Supprimer la dernière virgule
        query = query.rstrip(', ') + " WHERE id = %s"
        values.append(animal_id)
        
        self.cursor.execute(query, tuple(values))
        self.conn.commit()
        print(f"Animal avec ID {animal_id} mis à jour avec succès")

    def add_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite_max))
        self.conn.commit()
        print(f"Cage ajoutée avec succès")

    def remove_cage(self, cage_id):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (cage_id,))
        self.conn.commit()
        print(f"Cage avec ID {cage_id} supprimée avec succès")

    def update_cage(self, cage_id, superficie=None, capacite_max=None):
        query = "UPDATE cage SET "
        values = []
        if superficie:
            query += "superficie = %s, "
            values.append(superficie)
        if capacite_max:
            query += "capacite_max = %s, "
            values.append(capacite_max)

        # Supprimer la dernière virgule
        query = query.rstrip(', ') + " WHERE id = %s"
        values.append(cage_id)
        
        self.cursor.execute(query, tuple(values))
        self.conn.commit()
        print(f"Cage avec ID {cage_id} mise à jour avec succès")

    def get_all_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()
        
        # Formater les dates
        formatted_animals = []
        for animal in animals:
            animal_id, nom, race, id_cage, date_naissance, pays_origine = animal
            # Formater la date au format DD.MM.YYYY
            formatted_date = date_naissance.strftime("%d.%m.%Y")
            formatted_animals.append((animal_id, nom, race, id_cage, formatted_date, pays_origine))
        
        return formatted_animals

    def get_all_cages(self):
        query = "SELECT * FROM cage"
        self.cursor.execute(query)
        cages = self.cursor.fetchall()
        return cages

    def get_total_cage_area(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        total_area = self.cursor.fetchone()[0]
        print(f"La superficie totale des cages est de {total_area} m²")
        return total_area


# Test du programme
if __name__ == "__main__":
    zoo = Zoo()

    # Ajouter des cages
    zoo.add_cage(200, 5)
    zoo.add_cage(350, 8)

    # Ajouter des animaux
    zoo.add_animal('Lion', 'Panthera leo', 1, '2018-06-15', 'Tanzanie')
    zoo.add_animal('Elephant', 'Loxodonta africana', 2, '2015-05-10', 'Kenya')

    # Afficher tous les animaux avec la date formatée
    animals = zoo.get_all_animals()
    print("Liste des animaux :")
    for animal in animals:
        print(animal)

    # Afficher toutes les cages
    cages = zoo.get_all_cages()
    print("\nListe des cages :")
    for cage in cages:
        print(cage)

    # Calculer la superficie totale des cages
    zoo.get_total_cage_area()

    # Mise à jour d'un animal
    zoo.update_animal(1, nom='Lion Blanc')

    # Suppression d'un animal
    zoo.remove_animal(2)

    # Mise à jour d'une cage
    zoo.update_cage(1, capacite_max=6)

    # Suppression d'une cage
    zoo.remove_cage(2)
