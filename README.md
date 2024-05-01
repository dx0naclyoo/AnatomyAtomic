
API Для Сайта по Изучению и Практики Анатомии

API Docs - https://anatomyatomic.onrender.com/

Site - ""


DATABASE:

SQL architecture:

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/89c56761-5f32-4af8-95c1-478992202460)


TABLES:

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/605a14ea-99ff-4ff6-a2aa-bb1784941d81)

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/00dd88ce-dd43-438d-a3a2-92a97c9c3f12)


SECTION | Главы

id | name                   |description  |                                    
---+------------------------+-------------+
INT| TEXT                   |TEXT         |


TOPIC | Темы

id | name | slug | content | Section ID   |
---+------+------+------------------------+
INT| TEXT | TEXT | TEXT    | INT          |
