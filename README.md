
API Для Сайта по Изучению и Практики Анатомии

API Docs - https://anatomyatomic.onrender.com/

Site - ""



DATABASE:

SQL architecture:

DIAGRAM:

+----------+    One to Many     +-----------+
| Section  | ------------------ |  TOPIC    |
+----------+                    +-----------+


TABLES:

SECTION | Главы

id | name                   |description  |                                    
---+------------------------+-------------+
INT| TEXT                   |TEXT         |


TOPIC | Темы

id | name | slug | content | Section ID   |
---+------+------+------------------------+
INT| TEXT | TEXT | TEXT    | INT          |
