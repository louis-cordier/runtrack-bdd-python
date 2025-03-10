mysql> INSERT INTO etudiant (nom, age, email) 
    -> VALUES ('Martin Dupuis', 18, 'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM etudiant WHERE nom LIKE '%Dupuis';
+----+---------------+----------+------+---------------------------------+
| id | nom           | prenom   | Age  | email                           |
+----+---------------+----------+------+---------------------------------+
| 10 | Dupuis        | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
| 11 | Martin Dupuis | NULL     |   18 | martin.dupuis@laplateforme.io   |
+----+---------------+----------+------+---------------------------------+
2 rows in set (0.00 sec)

mysql> DELETE FROM etudiant WHERE id=11;
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM etudiant WHERE nom LIKE '%Dupuis';
+----+--------+----------+------+---------------------------------+
| id | nom    | prenom   | Age  | email                           |
+----+--------+----------+------+---------------------------------+
| 10 | Dupuis | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
| 12 | Dupuis | Martin   |   18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+------+---------------------------------+
2 rows in set (0.00 sec)

mysql> notee
