import mysql.connector
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()

    # Requête SQL pour récupérer les noms et capacités des salles
    query = "SELECT nom, capacite FROM salle;"
    cursor.execute(query)

    # Récupération des résultats
    salles = cursor.fetchall()

    # Affichage des résultats
    print("\nListe des salles et leurs capacités :")
    for salle in salles:
        print(f"Nom: {salle[0]}, Capacité: {salle[1]} places")

except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
