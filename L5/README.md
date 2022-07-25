# Лекція 3
25.07.2022


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