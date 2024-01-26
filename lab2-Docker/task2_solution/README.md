## Обученение нейронной сети 
Cемантическая сегментация - это задача анализа изображений, в которой мы классифицируем каждый пиксель изображения в класс. Например, человек - это один класс, мотоцикл - второй, а третий - фон. 

Одной из важных задач сегментации объектов является задача автономного управления автомобилем. Поэтому, в качестве входов, выбраны изображения перекрестков. В качестве модели семантической сегментации взята [FNC](https://machinelearningmastery.ru/efficient-method-for-running-fully-convolutional-networks-fcns-3174dc6a692b/).

На выход модели подаются трехканальные (rgb) изображения, которые нормализуются с помощью среднего значения и стандартного отклонения. Таким образом, размер входного сигнала равен [Ni x Ci x Hi x Wi]. 

На выходе мы получаем рультат [Nj=Ni x Cj x Hj x Wj]
- N - размер пакета
- WхH - размерность изображения.

Compose - это функция, которая принимает список, в котором каждый элемент имеет тип преобразований, и возвращает объект, через который мы можем передавать пакеты изображений, и все необходимые преобразования будут применены к изображениям из пакета.

## Запуск контейнера

1. Прописываем необходимый скрипт в Dockerfile и docker-compose.yml
2. Cобираем Docker-образ командой
```
docker build -t <тег_образа> .
```
3. Запускаем контейнер
```
docker-compose up
```

Как мы видим, после запуска в локальном директории появилась папка output

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/44859c34fdab226b72cc4baeec825618fec71849/lab2-Docker/task2_solution/result.jpg" waight="22" hight="14">

Результаты, полученные с помощью модели, представлены на рисунках ниже

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/6deca0f68d77dc41cde3da1268d72fcc351cf929/lab2-Docker/task2_solution/img/input.jpg">

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/6deca0f68d77dc41cde3da1268d72fcc351cf929/lab2-Docker/task2_solution/img/cat.jpg">

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/aadb2f6962777814d2513e6e7ca0ad44fec13f6e/lab2-Docker/task2_solution/output%20road%20img.jpg">


<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/aadb2f6962777814d2513e6e7ca0ad44fec13f6e/lab2-Docker/task2_solution/output%20cat%20img.jpg">
