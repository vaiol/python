# Лекція 2
### 13.07.2022


# Лекція 2

1. Запис лекції [https://youtu.be/H5RJn-12uyU](https://youtu.be/H5RJn-12uyU)
2. Посилання на презентацію [https://github.com/vaiol/python/blob/main/L2/L2.pdf](https://github.com/vaiol/python/blob/main/L2/L2.pdf)
3. Посилання на репозиторій з матеріалами лекції [https://github.com/vaiol/python/tree/main/L2](https://github.com/vaiol/python/tree/main/L2)

## Додаткові матеріали

[https://younglinux.info/python/variable](https://younglinux.info/python/variable)
[https://younglinux.info/python/operators](https://younglinux.info/python/operators)
[https://younglinux.info/python/if](https://younglinux.info/python/if)
[https://younglinux.info/python/while](https://younglinux.info/python/while)

[https://pythonworld.ru/osnovy/sintaksis-yazyka-python.html](https://pythonworld.ru/osnovy/sintaksis-yazyka-python.html)

[https://pythonworld.ru/tipy-dannyx-v-python/chisla-int-float-complex.html](https://pythonworld.ru/tipy-dannyx-v-python/chisla-int-float-complex.html)
[https://pythonworld.ru/tipy-dannyx-v-python/stroki-literaly-strok.html](https://pythonworld.ru/tipy-dannyx-v-python/stroki-literaly-strok.html)
[https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html](https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html)

[https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Использование_Python_в_качестве_калькулятора](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_Python_%D0%B2_%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B5_%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80%D0%B0)

[https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Строки](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%A1%D1%82%D1%80%D0%BE%D0%BA%D0%B8)
[https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1#Оператор_if](https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_if)

## Домашнє завдання

### Завдання 1

```python
# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перевірить певне число на те чи воно парне або непарне.

# Функція приймає на вхід будь яке число 
# і виводить в консоль строку типу 'Число Х є парним'.
# Наприклад:
#   oddOrEven(1) - > 'Число Х є непарним'
#   oddOrEven(20) - > 'Число Х є парним'
# Можна додавати свої тести за прикладом. 
# Потрібно врахувати обробку можливих помилок.

def oddOrEven(num):
    print('Напишіть логіку тут...')

oddOrEven(1) # 'Число Х є непарним'
oddOrEven(20) # 'Число Х є парним'
```

### Завдання 2

```python
# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перетворить вхідну строчку за певною логікою.

# Функція приймає на вхід будь яку строчку і виводить в консоль 
# за допомогою функції print()
#  оновлену версію цієї строчки.
# Якщо довжина строчки більша ніж 5 символів 
#    -> Потрібно вивести лише перші 5 символів та в кінці додати три точки (...).
# Якщо перша літера строчки U або u (регістр не важливий) 
#    -> Вивести всю строчку в Upper Case (верхній регістр)
# Якщо перша літера строчки L або l (регістр не важливий) 
#    -> Вивести всю строчку в Lower Case (нижній регістр)
# Якщо жодна умова вище не підходить - вивести строку без змін.
# Декілька умов можуть пересікатись!
# Можна додавати свої тести за прикладом. 
# Потрібно врахувати обробку можливих помилок.

# Наприклад:
#   transformStr('Testing string') - > 'Testi...' (довжина більше 5 символів)
#   transformStr('Lux') - > 'lux' (Починается на L)
#   transformStr('up') - > 'UP' (Починается на U)
#   transformStr('Luxery') - > 'luxer...' (Починается на L + довжина більше 5 символів)

def transformStr(str):
    print('Напишіть логіку тут...')

transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
transformStr('Lux') # 'lux' (Починается на L)
transformStr('up') # 'UP' (Починается на U)
transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)
```

### Завдання 3 (додаткове)

```python
# Напишіть функцію sumNum що задовільняє наступній умові:

# Дано ціле число num, 
# декілька кілька разів додайте всі його цифри, 
# доки в результаті не буде лише одна цифра, і поверніть її.

# Приклад 1
# sumNum(40) -> 4

# Для числа 40 потріботно повернути 4, чому?
# 1. 40 - розкладаємо на цифри -> 4, 0
# 2. Складаємо цифри 4 + 0 = 4
# 3. 4 - це одна цифра, повертаємо її

# Приклад 2
# sumNum(48) -> 3

# Для числа 48 потріботно повернути 3, чому?
# 1. 48 - розкладаємо на цифри -> 4, 8
# 2. Складаємо цифри 4 + 8 = 12
# 3. 12 - розкладаємо на цифри -> 1, 2
# 4. Складаємо цифри 1 + 2 = 3
# 5. 3 - це одна цифра, повертаємо її

# Приклад 3
# sumNum(2) -> 2

# Для числа 2 потріботно повернути 2, тому що число 2 складається з однієї цифри.

def sumNum(num):
    return num

print(sumNum(38) == 2) 
print(sumNum(40) == 4)
print(sumNum(48) == 3) 
print(sumNum(2) == 2)
```

### Завдання 4 (додаткове)

```python
# Напишіть функцію commonStr що задовільняє наступній умові:

# Дано дві строчки, поверніть нову строчку 
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку. 
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'

def commonStr(str1, str2):
    return ''

print(commonStr('loli', 'luck') == 'l') 
print(commonStr('good day', 'good morning') == 'god')
```