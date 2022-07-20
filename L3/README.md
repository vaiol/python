# Лекція 3
18.07.2022


## Матеріали
1. Запис лекції [https://youtu.be/HzBv9RuzAjE](https://youtu.be/HzBv9RuzAjE)  

## Додаткові матеріали
- https://pythonguide.rozh2sch.org.ua/#_%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8_%D1%96_%D0%BA%D0%BE%D1%80%D1%82%D0%B5%D0%B6%D1%96 
- https://pythonguide.rozh2sch.org.ua/#_%D1%86%D0%B8%D0%BA%D0%BB_for
- https://pythonguide.rozh2sch.org.ua/#_%D0%BE%D0%B1%D1%80%D0%BE%D0%B1%D0%BA%D0%B0_%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BE%D0%BA
- https://pythonguide.rozh2sch.org.ua/#_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97
- https://younglinux.info/python/list
- https://younglinux.info/python/for
- https://pythonworld.ru/osnovy/cikly-for-i-while-operatory-break-i-continue-volshebnoe-slovo-else.html
- https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
- https://pythonworld.ru/osnovy/indeksy-i-srezy.html
- https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html
- https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
- https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_range()
- https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9
- https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%B5%D0%B5_%D0%BE_%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0%D1%85


## ДЗ

1. Всі роботи мають бути запушені до репозиторію з назвою `python-hw-3` (повинен бути передчасно створений).
2. Дедлайн виконання завдання - 24.07.2022  24:00.

### Завдання 1

Файл: `calculate.py`
Оцінка: 50

Покращити програму `calculate` (файл [calculate_raw.py](https://github.com/vaiol/python/blob/main/L3/src/calculate_raw.py)) яка була створена на лекції функцією виконання арифметичної операції в одній строчці. А також розширена новими арифметичними операціями.  
Можна використовувати вихідний код вашої програми виконання відповідного ДЗ, але попередньо повинні бути виправлені помилки.  
Програма має задовольняти наступні потреби:  
1. Створити файл `calculate.py` 
1. Программа повина зчитувати аргументи командної строки (за допомогою модуля `sys`) і виконувати арифметичні операції.
1. Необхідна підтримка 5 базових арифметичних операцій: `+`, `-`, `*`, `/`, `%` (додавання, віднімання, множення, ділення, остача від ділення). Додано нову операцію - %.
1. Результат виконання арифметичної операції потрібно виводити у консоль.
1. Программа повинна адекватно оброблювати помилки.
1. Программа повинна запускатись наступним чином: `python calculate.py 2 + 2` або `python calculate.py 2+2`
1. Приклади:
    1. `python calculate.py 2 + 2` -> 4
    1. `python calculate.py 2 - 200` -> -198
    1.  `python calculate.py 2 * 8` -> 16
    1.  `python calculate.py 200 / 2` -> 100 
    1. `python calculate.py 3+3` -> 6
    1. `python calculate.py 100-20` -> 80
    1.  `python calculate.py 4*4` -> 16
    1.  `python calculate.py 25/2` -> 12.5 
1. Заборонено використовувати `eval` для обчислення результату.
1. Повинна бути створена і використана функція обчислення `def calc(left_operand, right_operand, operation)` яка повертає результат арифметичного обчислення.


### Завдання 2

Файл: `double_zero.py`
Оцінка: 25

Створіть функцію `def double_zero(array)` яка приймає цілочисельний масив і дублює всі нулі, повертаючи новий масив в якому нулі продубльювані, при дублювані всі інші елементи повинні бути зсунутті вправо.

Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі `double_zero.py` повина бути створена функція `def double_zero(array)` яка виконує необхідну логіку.

Приклади:
- `double_zero([1,0,2,3,0,4,5,0])` -> [1,0,0,2,3,0,0,4,5,0,0]
- `double_zero([1,0,2,3,0,4,5,0])` -> [1,0,0,2,3,0,0,4,5,0,0]
- `double_zero([1,2,3])` -> [1,2,3]


### Завдання 3

Файл: `remove_duplicates.py`
Оцінка: 25


Створіть функцію `def remove_duplicates(array)` яка приймає цілочисельний масив, відсортований у порядку зростання, видаліть дублікати чисел, щоб кожен унікальний елемент з’являвся лише один раз. Функція має повертати новий масив без дуплікатів чисел, відносний порядок елементів має бути незмінним

Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі `remove_duplicates.py` повина бути створена функція `def remove_duplicates(array)` яка виконує необхідну логіку.

Приклади:
- `remove_duplicates([1,1,2])` -> [1,2]
- `remove_duplicates([0,0,1,1,1,2,2,3,3,4])` -> [0,1,2,3,4]
- `remove_duplicates([1,1,1,1,1,1,1,1])` -> [1]


### Завдання 4 (додаткове)

Файл: `spiral.py`
Оцінка: 25


Створіть функцію `def spiral(matrix)` яка приймає цілочисельну матрицю розміром NxM та повертає масив в якому числа з матриці записані в порядку спіралі.
Матриця виглядає наступним чином:
```
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```
Це масив цілочисельних масивів. 
Наприклад матриця розміром 3x4 виглядає ось так:
```
[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
```
Порядок спіралі виглядає ось так:  
![m1](https://raw.githubusercontent.com/vaiol/python/main/L3/src/m1.png)  
   
     
![m2](https://raw.githubusercontent.com/vaiol/python/main/L3/src/m2.png)

Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі `spiral.py` повина бути створена функція `def spiral(matrix)` яка виконує необхідну логіку.

Приклади:
- `spiral([[1,2,3],[4,5,6],[7,8,9]])` -> [1,2,3,6,9,8,7,4,5]
- `spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])` -> [1,2,3,4,8,12,11,10,9,5,6,7]

