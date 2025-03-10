mysql> UPDATE etudiant 
    -> SET age = 20 
    -> WHERE nom = 'Betty Spaghetti';
Query OK, 0 rows affected (0.00 sec)
Rows matched: 0  Changed: 0  Warnings: 0

mysql> SELECT * FROM etudiant WHERE nom = 'Betty Spaghetti';
Empty set (0.00 sec)

mysql> UPDATE etudiant
    -> SET age = 20
    -> WHERE nom = 'Spaghetti';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM etudiant WHERE nom = 'Spaghetti';
+----+-----------+--------+------+---------------------------------+
| id | nom       | prenom | Age  | email                           |
+----+-----------+--------+------+---------------------------------+
|  6 | Spaghetti | Betty  |   20 | betty.spaghetti@laplateforme.io |
+----+-----------+--------+------+---------------------------------+
1 row in set (0.00 sec)

mysql> 
mysql> notee
