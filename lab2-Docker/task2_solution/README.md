## Обученение нейронной сети 
Cемантическая сегментация - это задача анализа изображений, в которой мы классифицируем каждый пиксель изображения в класс. Например, человек - это один класс, мотоцикл - второй, а третий - фон. 

Одной из важных задач сегментации объектов является задача автономного управления автомобилем. Поэтому, в качестве входов, выбраны изображения перекрестков. В качестве модели семантической сегментации взята [FNC](https://machinelearningmastery.ru/efficient-method-for-running-fully-convolutional-networks-fcns-3174dc6a692b/).

На выход модели подаются трехканальные (rgb) изображения, которые нормализуются с помощью среднего значения и стандартного отклонения. Таким образом, размер входного сигнала равен [Ni x Ci x Hi x Wi]. 

На выходе мы получаем рультат [Nj=Ni x Cj x Hj x Wj]
- N - размер пакета
- WхH - размерность изображения.

Compose - это функция, которая принимает список, в котором каждый элемент имеет тип преобразований, и возвращает объект, через который мы можем передавать пакеты изображений, и все необходимые преобразования будут применены к изображениям из пакета.

Результаты, полученные с помощью модели, представлены на рисунках ниже

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/6deca0f68d77dc41cde3da1268d72fcc351cf929/lab2-Docker/task2_solution/img/input.jpg">

<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/6deca0f68d77dc41cde3da1268d72fcc351cf929/lab2-Docker/task2_solution/img/cat.jpg">

<img src"https://github.com/MariaShaiina/ds_cours_2023/blob/aadb2f6962777814d2513e6e7ca0ad44fec13f6e/lab2-Docker/task2_solution/output%20road%20img.jpg">


<img src="https://github.com/MariaShaiina/ds_cours_2023/blob/aadb2f6962777814d2513e6e7ca0ad44fec13f6e/lab2-Docker/task2_solution/output%20cat%20img.jpg">
