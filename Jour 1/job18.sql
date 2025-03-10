mysql> DELETE FROM etudiant WHERE nom = 'Doe';
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM etudiant;
+----+-----------+----------+------+---------------------------------+
| id | nom       | prenom   | Age  | email                           |
+----+-----------+----------+------+---------------------------------+
|  6 | Spaghetti | Betty    |   20 | betty.spaghetti@laplateforme.io |
|  7 | Steak     | Chuck    |   45 | chuck.steak@laplateforme.io     |
|  9 | Barnes    | Binkie   |   16 | binkie.barnes@laplateforme.io   |
| 10 | Dupuis    | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
| 12 | Dupuis    | Martin   |   18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+------+---------------------------------+
5 rows in set (0.00 sec)

mysql> notee
