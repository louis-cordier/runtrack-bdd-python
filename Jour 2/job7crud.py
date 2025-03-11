# import mysql.connector
# from dotenv import load_dotenv
# import os

# # Charger les variables d'environnement depuis un fichier .env
# load_dotenv()

# class Employe:
#     def __init__(self):
#         # Connexion à la base de données
#         self.conn = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME")
#         )
#         self.cursor = self.conn.cursor()

#     def create_employe(self, nom, prenom, salaire, id_service):
#         query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
#         self.cursor.execute(query, (nom, prenom, salaire, id_service))
#         self.conn.commit()
#         print("Employé ajouté avec succès!")

#     def get_employes(self):
#         query = "SELECT * FROM employe"
#         self.cursor.execute(query)
#         return self.cursor.fetchall()

#     def get_employes_by_salary(self, salaire):
#         query = "SELECT * FROM employe WHERE salaire > %s"
#         self.cursor.execute(query, (salaire,))
#         return self.cursor.fetchall()

#     def update_employe_salary(self, id, new_salary):
#         query = "UPDATE employe SET salaire = %s WHERE id = %s"
#         self.cursor.execute(query, (new_salary, id))
#         self.conn.commit()
#         print(f"Le salaire de l'employé ID {id} a été mis à jour!")

#     def delete_employe(self, id):
#         query = "DELETE FROM employe WHERE id = %s"
#         self.cursor.execute(query, (id,))
#         self.conn.commit()
#         print(f"Employé ID {id} supprimé avec succès!")

#     def get_employes_with_services(self):
#         query = """SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service 
#                    FROM employe e 
#                    JOIN service s ON e.id_service = s.id"""
#         self.cursor.execute(query)
#         return self.cursor.fetchall()

#     def close(self):
#         self.cursor.close()
#         self.conn.close()


# # Exemple d'utilisation
# if __name__ == "__main__":
#     employe_db = Employe()

#     # Ajouter un employé
#     employe_db.create_employe('Lemoine', 'Sophie', 3200, 2)

#     # Récupérer tous les employés
#     employes = employe_db.get_employes()
#     print("Tous les employés :")
#     for employe in employes:
#         print(employe)

#     # Récupérer les employés avec salaire supérieur à 3000 €
#     employes_high_salary = employe_db.get_employes_by_salary(3000)
#     print("Employés avec salaire supérieur à 3000 € :")
#     for employe in employes_high_salary:
#         print(employe)

#     # Mettre à jour le salaire d'un employé
#     employe_db.update_employe_salary(1, 5000)

#     # Supprimer un employé
#     employe_db.delete_employe(2)

#     # Récupérer les employés et leurs services respectifs
#     employes_services = employe_db.get_employes_with_services()
#     print("Employés et leurs services :")
#     for employe in employes_services:
#         print(employe)

#     employe_db.close()

import mysql.connector
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Employe:
    def __init__(self):
        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME1")
        )
        self.cursor = self.conn.cursor()

    # Créer un employé
    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print("Employé ajouté avec succès!")

    # Récupérer tous les employés
    def get_employes(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # Récupérer les employés avec un salaire supérieur à un montant donné
    def get_employes_by_salary(self, salaire):
        query = "SELECT * FROM employe WHERE salaire > %s"
        self.cursor.execute(query, (salaire,))
        return self.cursor.fetchall()

    # Mettre à jour le salaire d'un employé
    def update_employe_salary(self, id, new_salary):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (new_salary, id))
        self.conn.commit()
        print(f"Le salaire de l'employé ID {id} a été mis à jour!")

    # Supprimer un employé par son ID
    def delete_employe(self, id):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.conn.commit()
        print(f"Employé ID {id} supprimé avec succès!")

    # Récupérer les employés et leurs services respectifs
    def get_employes_with_services(self):
        query = """SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service 
                   FROM employe e 
                   JOIN service s ON e.id_service = s.id"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation
if __name__ == "__main__":
    employe_db = Employe()

    # Ajouter un employé
    employe_db.create_employe('Lemoine', 'Sophie', 3200, 2)

    # Récupérer tous les employés
    employes = employe_db.get_employes()
    print("Tous les employés :")
    for employe in employes:
        print(employe)

    # Récupérer les employés avec salaire supérieur à 3000 €
    employes_high_salary = employe_db.get_employes_by_salary(3000)
    print("Employés avec salaire supérieur à 3000 € :")
    for employe in employes_high_salary:
        print(employe)

    # Mettre à jour le salaire d'un employé
    employe_db.update_employe_salary(1, 5000)

    # Supprimer un employé
    employe_db.delete_employe(2)

    # Récupérer les employés et leurs services respectifs
    employes_services = employe_db.get_employes_with_services()
    print("Employés et leurs services :")
    for employe in employes_services:
        print(employe)

    employe_db.close()
