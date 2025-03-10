mysql> SELECT * FROM etudiant 
    -> WHERE age BETWEEN 18 AND 25
    -> ORDER BY age ASC;
+----+-----------+----------+------+---------------------------------+
| id | nom       | prenom   | Age  | email                           |
+----+-----------+----------+------+---------------------------------+
|  8 | Doe       | John     |   18 | john.doe@laplateforme.io        |
| 12 | Dupuis    | Martin   |   18 | martin.dupuis@laplateforme.io   |
| 10 | Dupuis    | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
|  6 | Spaghetti | Betty    |   23 | betty.spaghetti@laplateforme.io |
+----+-----------+----------+------+---------------------------------+
4 rows in set (0.00 sec)

mysql> notee
