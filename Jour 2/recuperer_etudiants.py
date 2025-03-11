import mysql.connector
import os
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()
 
# Récupérer les informations depuis le .env
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

try:
    # Connexion à MySQL en utilisant les variables d'environnement
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    # Exécuter la requête pour récupérer tous les étudiants
    cursor.execute("SELECT * FROM etudiant")

    # Récupérer et afficher les résultats
    etudiants = cursor.fetchall()
    print("Liste des étudiants :")
    for etudiant in etudiants:
        print(etudiant)

except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    # Fermer la connexion proprement
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connexion MySQL fermée.")
