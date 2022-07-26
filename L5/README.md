# Лекція 5
25.07.2022

## Матеріали
1. Запис лекції [https://youtu.be/w9SGUvRfNws](https://youtu.be/w9SGUvRfNws)


## Додаткові матеріали

### Область видимості (scope)
- [https://pythonguide.rozh2sch.org.ua/#_простір_імен_і_області_видимості](https://pythonguide.rozh2sch.org.ua/#_%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%96%D1%80_%D1%96%D0%BC%D0%B5%D0%BD_%D1%96_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%96_%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%96)
- https://metanit.com/python/tutorial/2.9.php
- https://python-scripts.com/scope
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Области_видимости_и_пространства_имён_в_Python](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8_%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8_%D0%B8_%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0_%D0%B8%D0%BC%D1%91%D0%BD_%D0%B2_Python)
- https://younglinux.info/python/local-global


### Модулі
- https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html
- https://younglinux.info/python/modules
- [https://pythonguide.rozh2sch.org.ua/#_простір_імен_і_області_видимості](https://pythonguide.rozh2sch.org.ua/#_%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%96%D1%80_%D1%96%D0%BC%D0%B5%D0%BD_%D1%96_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%96_%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%96)
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Модули](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D0%B8)

### Дата і час
- [https://pythonguide.rozh2sch.org.ua/#_дата_й_час](https://pythonguide.rozh2sch.org.ua/#_%D0%B4%D0%B0%D1%82%D0%B0_%D0%B9_%D1%87%D0%B0%D1%81)
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Дата_и_время](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%94%D0%B0%D1%82%D0%B0_%D0%B8_%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)

### Lambda
- [https://pythonguide.rozh2sch.org.ua/#_анонімні_функції_інструкція_lambda](https://pythonguide.rozh2sch.org.ua/#_%D0%B0%D0%BD%D0%BE%D0%BD%D1%96%D0%BC%D0%BD%D1%96_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%97_%D1%96%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D1%96%D1%8F_lambda)
- [https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Модель_lambda](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_lambda)





## ДЗ

1. Всі роботи мають бути запушені до репозиторію вашого github з назвою `python-hw-5` (повинен бути передчасно створений).
1. Вирішення кожного завдання повино бути розміщено у окремому файлі. Файли повинні бути розміщені в корні репозиторію.
2. Дедлайн виконання завдання - 31.07.2022  24:00.
  
### Завдання 1

Файл: `popularity.py`
Оцінка: 50


Створіть функцію `def popularity(text)` яка приймає текст `text` і повертає унікальний массив строк відсортований за популярністью.

Уявіть що вам надсилають текст роману чи вірша і хочуть побачити найбільш популярні слова які зустрічаються у цьому тексті.

- Для початку ви повинні розбити текст на слова. Слова розділені звичайними пробілами.
- В тексті не будуть використовуватись точки або коми.
- Регістр слів не повинен мати значення. Тобто 'Apple' і 'aPPle' - одне слово.
- При формуванні результуючого массива слово повинно бути конвертовано в нижній регістр (lovercase). 
- Сортування повинно бути виконано від найпопулярніших слів до найменш популярних.
- Якщо слова мають однакову популярність, сортування повинно бути виконано за абеткою.


Приклади:
- `popularity('apple kiwi pineapple kiwi apple kiwi')` -> ['kiwi', 'apple', 'pineapple']
- `popularity('aPPle pine Apple kiwi Apple kiwi')` -> ['apple', 'kiwi', 'pine']
- `popularity('aPPle pine Apple kiwi Apple kiwi')` -> ['apple', 'kiwi', 'pine']
- `popularity('aab aaa aac aab aac aaa x')` -> ['aaa', 'aab', 'aac', 'x']



<sub>
Тестувати створену функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Ваш метод тестування ніяк не вплине на результат перевірки.
</sub>
<sub>
Головне що ви повинні мати для успішного виконання завдання це файл правильно названий всередині якого правильно названа функція яка виконує логіку.
Якщо ви допустите помилку в назвах, це призведе до незарахування завдання.
</sub>