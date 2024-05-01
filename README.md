
API Для Сайта по Изучению и Практики Анатомии

API Docs - https://anatomyatomic.onrender.com/

Site - ""


DATABASE: asd

SQL architecture:

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/89c56761-5f32-4af8-95c1-478992202460)


TABLES:

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/985c2e23-0862-449b-91f4-70ff90f8e614)

![image](https://github.com/dx0naclyoo/AnatomyAtomic/assets/145878340/00dd88ce-dd43-438d-a3a2-92a97c9c3f12)


SECTION | Главы

id | name                   |description  |                                    
---+------------------------+-------------+
INT| TEXT                   |TEXT         |


TOPIC | Темы

id | name | slug | content | Section ID   |
---+------+------+------------------------+
INT| TEXT | TEXT | TEXT    | INT          |
