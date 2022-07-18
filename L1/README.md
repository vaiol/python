# Лекція 1
### 11.07.2022

## Корисні матеріали

1. Запис лекції [https://youtu.be/YEn-YlgHCpw](https://youtu.be/YEn-YlgHCpw)
2. Посилання на презентацію [https://github.com/vaiol/python/blob/main/L1/L1.pdf](https://github.com/vaiol/python/blob/main/L1/L1.pdf)
3. Посилання на репозиторій з матеріалами лекції [https://github.com/vaiol/python](https://github.com/vaiol/python)

### Встановлюємо Python

1. Завантажити Python для windows [https://www.python.org/downloads/release/python-3105/](https://www.python.org/downloads/release/python-3105/)
2. Для mac os рекмоендую встновлювати через Homebrew та PyEnv [https://www.freecodecamp.org/news/python-version-on-mac-update/](https://www.freecodecamp.org/news/python-version-on-mac-update/)
    1. [https://brew.sh/](https://brew.sh/), встановлюємо homebrew командою `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` 
    2. встановлюємо `PyEnv` за допомогою homebrew `brew install pyenv`
    3. За допомогою `PyEnv` встановлюємо потрібну версію Python `pyenv install 3.10.5`

### Налаштовуємо середовище розробки

1. Встановлюємо PyCharm або Visual Studio Code за бажанням.
    1. PyCharm [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
    2. VS Code [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
        1. Для VS Code встановлюємо плагін `Python`

### Налаштовуємо GIT

1. Реєструємось на [https://github.com/](https://github.com/)
2. Встановлюємо git клієнт у випадку windows
3. Генеруємо ssh ключ [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
4. Додаємо ssh ключ до github [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
5. Тестуємо автентифікацію до github за допомогою команди `ssh -T git@github.com` [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

### Корисні посилання

- [https://itvdn.com/ru/video/basics-using-git](https://itvdn.com/ru/video/basics-using-git)
- [https://linuxize.com/post/how-to-configure-git-username-and-email/#:~:text=Git allows you to set,the change are not affected](https://linuxize.com/post/how-to-configure-git-username-and-email/#:~:text=Git%20allows%20you%20to%20set,the%20change%20are%20not%20affected)
- [https://www.youtube.com/watch?v=Z3ELWci34cM&ab_channel=CodingForEverybody](https://www.youtube.com/watch?v=Z3ELWci34cM&ab_channel=CodingForEverybody)[https://www.youtube.com/watch?v=KqzVaUTCPbQ&ab_channel=Loftschool](https://www.youtube.com/watch?v=KqzVaUTCPbQ&ab_channel=Loftschool)


## Домашнє завдання

### Завдання 1

1. Налаштувати середовище розробки. Python, git, github, ssh, VSCode або PyCharm.
2. Створити репозиторій на Github з назвою `python-hw-1`
3. Завантажити (запушити) файл [hello.py](http://hello.py) в корінь репозиторію, який виводить в консоль фразу `Hello World!`.
4. Скинути посиланная на репозиторій на пошту oleksandr@icecool.academy або у відповідь на цей лист.

Оцінка: 100 балів

### Завдання 2 (додатково)

1. У репозиторії `python-hw-1` стоворити файл `calculate.py` який повинен місти программу вирішення базових арифметичних операцій.
2. Программа повина зчитувати аргументи командної строки (за допомогою модуля `sys`) і виконувати арифметичні операції.
3. Необхідна підтримка 4 базових арифметичних операцій: +, -, *, / 
- додавання, віднімання, множення, ділення.
4. Результат виконання арифметичної операції потрібно виводити у консоль.
5. Программа повинна адекватно оброблювати помилки.
6. Программа повинна запускатись наступним чином: `python calculate.py 2 + 2` 
7. Тестові запуски:
    1. `python calculate.py 2 + 2` -> 4
    2. `python calculate.py 2 - 200` -> -198
    3.  `python calculate.py 2 * 8` -> 16
    4.  `python calculate.py 200 / 2` -> 100 

Оцінка: 25 балів

Дедлайн: неділя, 17.07.2022, 24:00