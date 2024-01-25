## Описание полученных результатов 

В первой чати лаборатоной работы был собран и запущен Docker контейнер на базе образа Ubuntu 22.04. Реализован и запущен внутри контейнера алгоритм обработки изображения. Результирующие изображения сохранены в директорий хоста и в локальный директорий контейнера.


Обработка изображения включала следующие этапы:

1. Преобразовать изображение в градации серого.
2. Построить гистограмму значений яркости пикселей.
3. Сделать пороговую обработку методом Otsu - функция OpenCV (пороговое значение указано на рисунке 1).
4. Т.к. исходное изображение обладает очень слабым контрастом, то последний шаг - повысить контрастность изображения.

_________________________
Рисунок 1 - Результат запуска контейнера 

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/9a4bebb15bbeaa559b363ffcca51c2b92f5946a2/lab2-Docker/img/py_res.jpg">

_________________________
Рисунок 2 - Исходное изображение

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/9a4bebb15bbeaa559b363ffcca51c2b92f5946a2/lab2-Docker/img/orig_img.jpg">

_________________________
Рисунок 3 - Пороговая обработка

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/9a4bebb15bbeaa559b363ffcca51c2b92f5946a2/lab2-Docker/img/threshold%20img.jpg">

_________________________
Рисунок 4 - Результат обработки

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/9a4bebb15bbeaa559b363ffcca51c2b92f5946a2/lab2-Docker/img/result%20img.jpg">

_________________________

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/9a4bebb15bbeaa559b363ffcca51c2b92f5946a2/lab2-Docker/img/results_1.png">

