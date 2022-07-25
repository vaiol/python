# Лекція 4
20.07.2022


## Матеріали
1. Запис лекції [https://youtu.be/jUGG8ZZ0MlU](https://youtu.be/jUGG8ZZ0MlU)
































\


## Додаткові матеріали

### Кортежі (tuple)
- [https://pythonguide.rozh2sch.org.ua/#_списки_і_кортежі](https://pythonguide.rozh2sch.org.ua/#_%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8_%D1%96_%D0%BA%D0%BE%D1%80%D1%82%D0%B5%D0%B6%D1%96)
- https://younglinux.info/python/tuple
- https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Кортежи_и_последовательности](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9A%D0%BE%D1%80%D1%82%D0%B5%D0%B6%D0%B8_%D0%B8_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8)

### Словники (dictionary)
- [https://pythonguide.rozh2sch.org.ua/#_словники_і_множини](https://pythonguide.rozh2sch.org.ua/#_%D1%81%D0%BB%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA%D0%B8_%D1%96_%D0%BC%D0%BD%D0%BE%D0%B6%D0%B8%D0%BD%D0%B8)
- https://younglinux.info/python/dictionary
- https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Словари](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8)


### Множини (set)
- [https://pythonguide.rozh2sch.org.ua/#_множини](https://pythonguide.rozh2sch.org.ua/#_%D0%BC%D0%BD%D0%BE%D0%B6%D0%B8%D0%BD%D0%B8)
- https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Множества](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0)

### Summary data types
- https://dementiy.github.io/lectures/immutable-types/
- https://dementiy.github.io/lectures/mutable-types/

### Hash
- https://pythobyte.com/python-hash-function-09311/


## ДЗ

1. Всі роботи мають бути запушені до репозиторію вашого github з назвою `python-hw-4` (повинен бути передчасно створений).
1. Вирішення кожного завдання повино бути розміщено у окремому файлі.
2. Дедлайн виконання завдання - 29.07.2022  24:00.

### Завдання 1

Файл: `twoSum.py`
Оцінка: 50

Створіть функцію `def twoSum(nums, target)` яка приймає цілочисельний масив, і ціле число, а повертає індекси двох чисел массиву так, щоб їх сума дала передане ціле число.

- Ви можете припустити, що кожен вхід матиме рівно одне рішення, 
- Ви не можете використовувати той самий елемент двічі.
- Ви можете повернути відповідь у будь-якому порядку.

- Завдання було описано в файлі https://github.com/vaiol/python/blob/main/L4/src/05_two_sum.py
- Також розбір на лекції https://youtu.be/jUGG8ZZ0MlU?t=8008  

Приклади:
- `twoSum([1, 2, 3], 4)` -> [0, 2]
- `twoSum([2, 7, 11, 15], 9)` -> [0, 1]
- `twoSum([3, 2, 4], 6)` -> [1, 2]
- `twoSum([3, 3], 6)` -> [0, 1]



<sub>
Тестувати створену функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Ваш метод тестування ніяк не вплине на результат перевірки.
</sub>
<sub>
Головне що ви повинні мати для успішного виконання завдання це файл правильно названий всередині якого правильно названа функція яка виконує логіку.
Якщо ви допустите помилку в назвах, це призведе до незарахування завдання.
</sub>
