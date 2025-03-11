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

    # Exécuter la requête pour calculer la superficie totale
    query = "SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') AS message FROM etage;"
    cursor.execute(query)

    # Récupérer le résultat
    result = cursor.fetchone()

    # Affichage du message
    print(result[0])

except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
