# import mysql.connector
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement (fichier .env)
# load_dotenv()

# class Store:
#     def __init__(self):
#         try:
#             self.conn = mysql.connector.connect(
#                 host=os.getenv("DB_HOST"),
#                 user=os.getenv("DB_USER"),
#                 password=os.getenv("DB_PASSWORD"),
#                 database=os.getenv("DB_NAME")
#             )
#             self.cursor = self.conn.cursor()
#             print("✅ Connexion à la base de données réussie")
#             self.create_tables()
#         except mysql.connector.Error as e:
#             print(f"❌ Erreur de connexion : {e}")

#     def create_tables(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS category (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255) NOT NULL
#             );
#         """)
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS product (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255) NOT NULL,
#                 description TEXT,
#                 price INT NOT NULL,
#                 quantity INT NOT NULL,
#                 id_category INT,
#                 FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE SET NULL
#             );
#         """)
#         self.conn.commit()

#     def add(self, table, **values):
#         columns = ', '.join(values.keys())
#         placeholders = ', '.join(['%s'] * len(values))
#         query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
#         self.cursor.execute(query, tuple(values.values()))
#         self.conn.commit()

#     def update(self, table, record_id, **values):
#         set_clause = ', '.join([f"{k} = %s" for k in values])
#         query = f"UPDATE {table} SET {set_clause} WHERE id = %s"
#         self.cursor.execute(query, tuple(values.values()) + (record_id,))
#         self.conn.commit()

#     def delete(self, table, record_id):
#         self.cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
#         self.conn.commit()

#     def get_all(self, table):
#         self.cursor.execute(f"SELECT * FROM {table}")
#         return self.cursor.fetchall()

#     def display_products(self):
#         self.cursor.execute("""
#             SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
#             FROM product
#             LEFT JOIN category ON product.id_category = category.id
#         """)
#         products = self.cursor.fetchall()
#         print("\n📦 Liste des produits :")
#         for p in products:
#             print(f"({p[0]}) {p[1]} - {p[2]} | {p[3]}€ | Stock: {p[4]} | Catégorie: {p[5] if p[5] else 'Aucune'}")

#     def display_categories(self):
#         categories = self.get_all("category")
#         print("\n📂 Liste des catégories :")
#         for c in categories:
#             print(f"({c[0]}) {c[1]}")

#     def total_stock_value(self):
#         self.cursor.execute("SELECT SUM(price * quantity) FROM product")
#         total = self.cursor.fetchone()[0]
#         print(f"\n💰 Valeur totale du stock : {total}€")
#         return total


# # 🏪 **TEST DU PROGRAMME**
# if __name__ == "__main__":
#     store = Store()

#     # Ajouter des catégories
#     store.add("category", name="Électronique")
#     store.add("category", name="Vêtements")

#     # Ajouter des produits
#     store.add("product", name="Ordinateur", description="PC Gamer", price=1200, quantity=5, id_category=1)
#     store.add("product", name="T-shirt", description="Coton bio", price=25, quantity=50, id_category=2)

#     # Afficher les produits et catégories
#     store.display_products()
#     store.display_categories()

#     # Valeur du stock
#     store.total_stock_value()

#     # Mise à jour d'un produit et suppression
#     store.update("product", 1, price=1100, quantity=4)
#     store.delete("product", 2)

#     # Suppression d'une catégorie
#     store.delete("category", 2)

# -------------------------Version 2 ------------------------------------------
# import tkinter as tk
# from tkinter import ttk, messagebox
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement
# load_dotenv()

# class StoreApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gestion des Stocks")
#         self.root.geometry("700x500")
        
#         # Connexion à la base de données
#         self.conn = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME")
#         )
#         self.cursor = self.conn.cursor()
        
#         # Interface graphique
#         self.create_widgets()
#         self.display_products()
    
#     def create_widgets(self):
#         # Tableau des produits
#         columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
#         self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
#         for col in columns:
#             self.tree.heading(col, text=col)
#         self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Boutons de gestion
#         btn_frame = tk.Frame(self.root)
#         btn_frame.pack(pady=10)
        
#         tk.Button(btn_frame, text="Ajouter", command=self.add_product).grid(row=0, column=0, padx=5)
#         tk.Button(btn_frame, text="Modifier", command=self.update_product).grid(row=0, column=1, padx=5)
#         tk.Button(btn_frame, text="Supprimer", command=self.delete_product).grid(row=0, column=2, padx=5)
    
#     def display_products(self):
#         self.tree.delete(*self.tree.get_children())
#         self.cursor.execute("""
#             SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
#             FROM product
#             LEFT JOIN category ON product.id_category = category.id
#         """)
#         for row in self.cursor.fetchall():
#             self.tree.insert("", tk.END, values=row)
    
#     def add_product(self):
#         self.product_form("Ajouter un produit")
    
#     def update_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à modifier.")
#             return
#         values = self.tree.item(selected_item[0], "values")
#         self.product_form("Modifier le produit", values)
    
#     def delete_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à supprimer.")
#             return
#         product_id = self.tree.item(selected_item[0], "values")[0]
#         self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
#         self.conn.commit()
#         self.display_products()
#         messagebox.showinfo("Succès", "Produit supprimé avec succès")
    
#     def product_form(self, title, values=None):
#         form = tk.Toplevel(self.root)
#         form.title(title)
#         form.geometry("300x300")
        
#         tk.Label(form, text="Nom").pack()
#         name_entry = tk.Entry(form)
#         name_entry.pack()
        
#         tk.Label(form, text="Description").pack()
#         desc_entry = tk.Entry(form)
#         desc_entry.pack()
        
#         tk.Label(form, text="Prix").pack()
#         price_entry = tk.Entry(form)
#         price_entry.pack()
        
#         tk.Label(form, text="Quantité").pack()
#         quantity_entry = tk.Entry(form)
#         quantity_entry.pack()
        
#         tk.Label(form, text="ID Catégorie").pack()
#         category_entry = tk.Entry(form)
#         category_entry.pack()
        
#         if values:
#             name_entry.insert(0, values[1])
#             desc_entry.insert(0, values[2])
#             price_entry.insert(0, values[3])
#             quantity_entry.insert(0, values[4])
#             category_entry.insert(0, values[5])
        
#         def save_product():
#             name = name_entry.get()
#             desc = desc_entry.get()
#             price = int(price_entry.get())
#             quantity = int(quantity_entry.get())
#             category_id = int(category_entry.get())
            
#             if values:
#                 self.cursor.execute("""
#                     UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s
#                 """, (name, desc, price, quantity, category_id, values[0]))
#             else:
#                 self.cursor.execute("""
#                     INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)
#                 """, (name, desc, price, quantity, category_id))
            
#             self.conn.commit()
#             self.display_products()
#             form.destroy()
        
#         tk.Button(form, text="Enregistrer", command=save_product).pack()

# # Lancer l'application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = StoreApp(root)
#     root.mainloop()

# --------------------------------Version 3 -----------------------------------4*

# import tkinter as tk
# from tkinter import ttk, messagebox
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement
# load_dotenv()

# class StoreApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gestion des Stocks")
#         self.root.geometry("700x500")
        
#         # Connexion à la base de données
#         self.conn = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME")
#         )
#         self.cursor = self.conn.cursor()
        
#         # Interface graphique
#         self.create_widgets()
#         self.display_products()
    
#     def create_widgets(self):
#         # Tableau des produits
#         columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
#         self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
#         for col in columns:
#             self.tree.heading(col, text=col)
#         self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Boutons de gestion
#         btn_frame = tk.Frame(self.root)
#         btn_frame.pack(pady=10)
        
#         tk.Button(btn_frame, text="Ajouter", command=self.add_product).grid(row=0, column=0, padx=5)
#         tk.Button(btn_frame, text="Modifier", command=self.update_product).grid(row=0, column=1, padx=5)
#         tk.Button(btn_frame, text="Supprimer", command=self.delete_product).grid(row=0, column=2, padx=5)
    
#     def display_products(self):
#         self.tree.delete(*self.tree.get_children())
#         self.cursor.execute("""
#             SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
#             FROM product
#             LEFT JOIN category ON product.id_category = category.id
#         """)
#         for row in self.cursor.fetchall():
#             self.tree.insert("", tk.END, values=row)
    
#     def add_product(self):
#         self.product_form("Ajouter un produit")
    
#     def update_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à modifier.")
#             return
#         values = self.tree.item(selected_item[0], "values")
#         self.product_form("Modifier le produit", values)
    
#     def delete_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à supprimer.")
#             return
#         product_id = self.tree.item(selected_item[0], "values")[0]
#         self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
#         self.conn.commit()
#         self.display_products()
#         messagebox.showinfo("Succès", "Produit supprimé avec succès")
    
#     def product_form(self, title, values=None):
#         form = tk.Toplevel(self.root)
#         form.title(title)
#         form.geometry("300x300")
        
#         tk.Label(form, text="Nom").pack()
#         name_entry = tk.Entry(form)
#         name_entry.pack()
        
#         tk.Label(form, text="Description").pack()
#         desc_entry = tk.Entry(form)
#         desc_entry.pack()
        
#         tk.Label(form, text="Prix").pack()
#         price_entry = tk.Entry(form)
#         price_entry.pack()
        
#         tk.Label(form, text="Quantité").pack()
#         quantity_entry = tk.Entry(form)
#         quantity_entry.pack()
        
#         # Récupérer les catégories depuis la BDD
#         self.cursor.execute("SELECT id, name FROM category")
#         categories = self.cursor.fetchall()  # Liste des catégories [(1, "Électronique"), (2, "Vêtements")]

#         category_dict = {name: cat_id for cat_id, name in categories}  # Associe Nom → ID
#         category_names = list(category_dict.keys())  # Liste des noms de catégories

#         tk.Label(form, text="Catégorie").pack()
#         category_combo = ttk.Combobox(form, values=category_names, state="readonly")  # Menu déroulant
#         category_combo.pack()

#         # Si on modifie un produit existant, pré-remplir les champs
#         if values:
#             name_entry.insert(0, values[1])
#             desc_entry.insert(0, values[2])
#             price_entry.insert(0, values[3])
#             quantity_entry.insert(0, values[4])
#             category_combo.set(values[5])  # Mettre la catégorie actuelle

#         def save_product():
#             name = name_entry.get()
#             desc = desc_entry.get()
#             price = int(price_entry.get())
#             quantity = int(quantity_entry.get())
#             category_name = category_combo.get()  # Récupérer le nom sélectionné
#             category_id = category_dict.get(category_name)  # Trouver l'ID correspondant

#             if values:  # Modification
#                 self.cursor.execute("""
#                     UPDATE product 
#                     SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s 
#                     WHERE id=%s
#                 """, (name, desc, price, quantity, category_id, values[0]))
#             else:  # Ajout
#                 self.cursor.execute("""
#                     INSERT INTO product (name, description, price, quantity, id_category) 
#                     VALUES (%s, %s, %s, %s, %s)
#                 """, (name, desc, price, quantity, category_id))

#             self.conn.commit()
#             self.display_products()
#             form.destroy()

#         tk.Button(form, text="Enregistrer", command=save_product).pack()

# # Lancer l'application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = StoreApp(root)
#     root.mainloop()

# -------------------------------------Version 4-------------------------------------

# import tkinter as tk
# from tkinter import ttk, messagebox
# import mysql.connector
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement
# load_dotenv()

# class StoreApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gestion des Stocks")
#         self.root.geometry("700x500")
        
#         # Connexion à la base de données
#         self.conn = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME")
#         )
#         self.cursor = self.conn.cursor()
        
#         # Interface graphique
#         self.create_widgets()
#         self.display_products()
    
#     def create_widgets(self):
#         # Tableau des produits
#         columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
#         self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
#         for col in columns:
#             self.tree.heading(col, text=col)
#         self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Boutons de gestion
#         btn_frame = tk.Frame(self.root)
#         btn_frame.pack(pady=10)
        
#         tk.Button(btn_frame, text="Ajouter", command=self.add_product).grid(row=0, column=0, padx=5)
#         tk.Button(btn_frame, text="Modifier", command=self.update_product).grid(row=0, column=1, padx=5)
#         tk.Button(btn_frame, text="Supprimer", command=self.delete_product).grid(row=0, column=2, padx=5)
#         tk.Button(btn_frame, text="Ajouter une catégorie", command=self.add_category).grid(row=0, column=3, padx=5)
    
#     def display_products(self):
#         self.tree.delete(*self.tree.get_children())
#         self.cursor.execute("""
#             SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
#             FROM product
#             LEFT JOIN category ON product.id_category = category.id
#         """)
#         for row in self.cursor.fetchall():
#             self.tree.insert("", tk.END, values=row)
    
#     def add_product(self):
#         self.product_form("Ajouter un produit")
    
#     def update_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à modifier.")
#             return
#         values = self.tree.item(selected_item[0], "values")
#         self.product_form("Modifier le produit", values)
    
#     def delete_product(self):
#         selected_item = self.tree.selection()
#         if not selected_item:
#             messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à supprimer.")
#             return
#         product_id = self.tree.item(selected_item[0], "values")[0]
#         self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
#         self.conn.commit()
#         self.display_products()
#         messagebox.showinfo("Succès", "Produit supprimé avec succès")
    
#     def product_form(self, title, values=None):
#         form = tk.Toplevel(self.root)
#         form.title(title)
#         form.geometry("300x350")
        
#         tk.Label(form, text="Nom").pack()
#         name_entry = tk.Entry(form)
#         name_entry.pack()
        
#         tk.Label(form, text="Description").pack()
#         desc_entry = tk.Entry(form)
#         desc_entry.pack()
        
#         tk.Label(form, text="Prix").pack()
#         price_entry = tk.Entry(form)
#         price_entry.pack()
        
#         tk.Label(form, text="Quantité").pack()
#         quantity_entry = tk.Entry(form)
#         quantity_entry.pack()
        
#         # Récupérer les catégories depuis la BDD
#         self.cursor.execute("SELECT id, name FROM category")
#         categories = self.cursor.fetchall()
#         category_dict = {name: cat_id for cat_id, name in categories}
#         category_names = list(category_dict.keys())

#         tk.Label(form, text="Catégorie").pack()
#         category_combo = ttk.Combobox(form, values=category_names, state="readonly")
#         category_combo.pack()

#         # Ajouter une catégorie depuis cette fenêtre
#         tk.Button(form, text="Ajouter une catégorie", command=self.add_category).pack(pady=5)

#         if values:
#             name_entry.insert(0, values[1])
#             desc_entry.insert(0, values[2])
#             price_entry.insert(0, values[3])
#             quantity_entry.insert(0, values[4])
#             category_combo.set(values[5])

#         def save_product():
#             name = name_entry.get()
#             desc = desc_entry.get()
#             price = int(price_entry.get())
#             quantity = int(quantity_entry.get())
#             category_name = category_combo.get()
#             category_id = category_dict.get(category_name)

#             if category_id is None:
#                 messagebox.showerror("Erreur", "Veuillez sélectionner une catégorie valide.")
#                 return

#             if values:
#                 self.cursor.execute("""
#                     UPDATE product 
#                     SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s 
#                     WHERE id=%s
#                 """, (name, desc, price, quantity, category_id, values[0]))
#             else:
#                 self.cursor.execute("""
#                     INSERT INTO product (name, description, price, quantity, id_category) 
#                     VALUES (%s, %s, %s, %s, %s)
#                 """, (name, desc, price, quantity, category_id))

#             self.conn.commit()
#             self.display_products()
#             form.destroy()

#         tk.Button(form, text="Enregistrer", command=save_product).pack()

#     def add_category(self):
#         """Ajoute une nouvelle catégorie dans la base de données."""
#         category_form = tk.Toplevel(self.root)
#         category_form.title("Ajouter une catégorie")
#         category_form.geometry("300x150")

#         tk.Label(category_form, text="Nom de la catégorie").pack()
#         category_entry = tk.Entry(category_form)
#         category_entry.pack()

#         def save_category():
#             category_name = category_entry.get().strip()
#             if not category_name:
#                 messagebox.showerror("Erreur", "Le nom de la catégorie ne peut pas être vide.")
#                 return
            
#             # Vérifier si la catégorie existe déjà
#             self.cursor.execute("SELECT id FROM category WHERE name = %s", (category_name,))
#             if self.cursor.fetchone():
#                 messagebox.showwarning("Info", "Cette catégorie existe déjà.")
#                 category_form.destroy()
#                 return

#             # Ajouter la catégorie
#             self.cursor.execute("INSERT INTO category (name) VALUES (%s)", (category_name,))
#             self.conn.commit()
#             messagebox.showinfo("Succès", "Catégorie ajoutée avec succès.")

#             category_form.destroy()

#         tk.Button(category_form, text="Ajouter", command=save_category).pack()

# # Lancer l'application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = StoreApp(root)
#     root.mainloop()

# ----------------------------Version 5--------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
from dotenv import load_dotenv
import csv
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Charger les variables d'environnement
load_dotenv()

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Stocks")
        self.root.geometry("700x500")
        
        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor()
        
        # Interface graphique
        self.create_widgets()
        self.display_products()
    
    def create_widgets(self):
        # Tableau des produits
        columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Filtre de catégorie
        self.category_filter_label = tk.Label(self.root, text="Filtrer par catégorie:")
        self.category_filter_label.pack(pady=5)
        
        self.category_filter_combo = ttk.Combobox(self.root, state="readonly")
        self.category_filter_combo.bind("<<ComboboxSelected>>", self.filter_products_by_category)
        self.category_filter_combo.pack(pady=5)
        
        # Boutons de gestion
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Ajouter", command=self.add_product).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Modifier", command=self.update_product).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Supprimer", command=self.delete_product).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Ajouter une catégorie", command=self.add_category).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Exporter CSV", command=self.export_to_csv).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Afficher Graphique", command=self.show_graph).grid(row=0, column=5, padx=5)
    
    def display_products(self, category_filter=None):
        self.tree.delete(*self.tree.get_children())
        query = """
            SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
            FROM product
            LEFT JOIN category ON product.id_category = category.id
        """
        params = ()
        if category_filter:
            query += " WHERE category.name = %s"
            params = (category_filter,)
        
        self.cursor.execute(query, params)
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
    
    def filter_products_by_category(self, event):
        selected_category = self.category_filter_combo.get()
        self.display_products(selected_category)
    
    def add_product(self):
        self.product_form("Ajouter un produit")
    
    def update_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à modifier.")
            return
        values = self.tree.item(selected_item[0], "values")
        self.product_form("Modifier le produit", values)
    
    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un produit à supprimer.")
            return
        product_id = self.tree.item(selected_item[0], "values")[0]
        self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        self.conn.commit()
        self.display_products()
        messagebox.showinfo("Succès", "Produit supprimé avec succès")
    
    def product_form(self, title, values=None):
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("300x350")
        
        tk.Label(form, text="Nom").pack()
        name_entry = tk.Entry(form)
        name_entry.pack()
        
        tk.Label(form, text="Description").pack()
        desc_entry = tk.Entry(form)
        desc_entry.pack()
        
        tk.Label(form, text="Prix").pack()
        price_entry = tk.Entry(form)
        price_entry.pack()
        
        tk.Label(form, text="Quantité").pack()
        quantity_entry = tk.Entry(form)
        quantity_entry.pack()
        
        # Récupérer les catégories depuis la BDD
        self.cursor.execute("SELECT id, name FROM category")
        categories = self.cursor.fetchall()
        category_dict = {name: cat_id for cat_id, name in categories}
        category_names = list(category_dict.keys())

        tk.Label(form, text="Catégorie").pack()
        category_combo = ttk.Combobox(form, values=category_names, state="readonly")
        category_combo.pack()

        # Ajouter une catégorie depuis cette fenêtre
        tk.Button(form, text="Ajouter une catégorie", command=self.add_category).pack(pady=5)

        if values:
            name_entry.insert(0, values[1])
            desc_entry.insert(0, values[2])
            price_entry.insert(0, values[3])
            quantity_entry.insert(0, values[4])
            category_combo.set(values[5])

        def save_product():
            name = name_entry.get()
            desc = desc_entry.get()
            price = int(price_entry.get())
            quantity = int(quantity_entry.get())
            category_name = category_combo.get()
            category_id = category_dict.get(category_name)

            if category_id is None:
                messagebox.showerror("Erreur", "Veuillez sélectionner une catégorie valide.")
                return

            if values:
                self.cursor.execute("""
                    UPDATE product 
                    SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s 
                    WHERE id=%s
                """, (name, desc, price, quantity, category_id, values[0]))
            else:
                self.cursor.execute("""
                    INSERT INTO product (name, description, price, quantity, id_category) 
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, desc, price, quantity, category_id))

            self.conn.commit()
            self.display_products()
            form.destroy()

        tk.Button(form, text="Enregistrer", command=save_product).pack()

    def add_category(self):
        """Ajoute une nouvelle catégorie dans la base de données."""
        category_form = tk.Toplevel(self.root)
        category_form.title("Ajouter une catégorie")
        category_form.geometry("300x150")

        tk.Label(category_form, text="Nom de la catégorie").pack()
        category_entry = tk.Entry(category_form)
        category_entry.pack()

        def save_category():
            category_name = category_entry.get().strip()
            if not category_name:
                messagebox.showerror("Erreur", "Le nom de la catégorie ne peut pas être vide.")
                return
            
            # Vérifier si la catégorie existe déjà
            self.cursor.execute("SELECT id FROM category WHERE name = %s", (category_name,))
            if self.cursor.fetchone():
                messagebox.showwarning("Info", "Cette catégorie existe déjà.")
                category_form.destroy()
                return

            # Ajouter la catégorie
            self.cursor.execute("INSERT INTO category (name) VALUES (%s)", (category_name,))
            self.conn.commit()
            messagebox.showinfo("Succès", "Catégorie ajoutée avec succès.")

            category_form.destroy()

        tk.Button(category_form, text="Ajouter", command=save_category).pack()

    def export_to_csv(self):
        """Exporte les produits en stock dans un fichier CSV."""
        self.cursor.execute("""
            SELECT product.id, product.name, product.description, product.price, product.quantity, category.name
            FROM product
            LEFT JOIN category ON product.id_category = category.id
        """)
        products = self.cursor.fetchall()
        
        with open('products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"])
            for product in products:
                writer.writerow(product)
        
        messagebox.showinfo("Succès", "Les produits ont été exportés vers 'products.csv'.")

    def show_graph(self):
        """Affiche un graphique représentant la répartition des produits par catégorie."""
        self.cursor.execute("""
            SELECT category.name, COUNT(*) 
            FROM product
            LEFT JOIN category ON product.id_category = category.id
            GROUP BY category.name
        """)
        data = self.cursor.fetchall()
        
        categories = [item[0] for item in data]
        counts = [item[1] for item in data]
        
        fig, ax = plt.subplots()
        ax.bar(categories, counts)
        ax.set_title('Répartition des produits par catégorie')
        ax.set_xlabel('Catégorie')
        ax.set_ylabel('Nombre de produits')
        
        # Intégrer le graphique dans l'interface Tkinter
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.get_tk_widget().pack()
        canvas.draw()

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()


# Description MCD
# PRODUCT représente la table des produits avec les colonnes id, name, description, price, quantity,
# et id_category qui est une clé étrangère.
# CATEGORY représente les catégories de produits, avec un id et un name.
# La relation PRODUCT ||--|{ CATEGORY signifie qu'un produit appartient à une seule catégorie,''  mais qu'une catégorie
# peut avoir plusieurs produits.