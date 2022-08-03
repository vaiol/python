# Лекція 8
03.08.2022

## Матеріали
1. Запис лекції [to_be_announced]


## ДЗ
https://github.com/vaiol/python/tree/main/L7


## Commands
- `python -m pip --version` - перевірка чи встановлений PIP
- `python -m venv .venv` - створення віртуального оточення для проєкту
- `source .venv/bin/activate` - вхід у віртуальне оточення
- `deactivate` - вихід з віртуального оточення
- `pip install <package_name>` -  встановлюємо певну залежність
- `pip freeze` - показуємо залежності для requirements.txt
- `pip install -r requirements.txt` - встановлюємо залежності з файлу
- `python -m unittest <file_name>` - запускаємо автотести
- `python -m unittest <file_name> -v` - запускаємо автотести, більше детальний вивід

## Пакети
- https://pypi.org/ - шувкаємо пакети тут
- `flake8` - лінтер PEP8
- `pylint` - лінтер PEP8, показує більше помилок
- `mypy` - тестує наш код на помилки типів
- `black` - автоматично виправляє помилки та форматує код


## Тестування
### Available asserts
- `assertEqual(a, b)` -> `a == b`
- `assertNotEqual(a, b)` -> `a != b`
- `assertTrue(x)` -> `bool(x) is True`
- `assertFalse(x)` -> `bool(x) is False`
- `assertIs(a, b)` -> `a is b`
- `assertIsNot(a, b)` -> `a is not b`
- `assertIsNone(x)` -> `x is None`
- `assertIsNotNone(x)` -> `x is not None`
- `assertIn(a, b)` -> `a in b`
- `assertNotIn(a, b)` -> `a not in b`
- `assertIsInstance(a, b)` -> `isinstance(a, b)`
- `assertNotIsInstance(a, b)` -> `not isinstance(a, b)`
- `assertRaises(exc, fun, *args, **kwds)` -> `fun(*args, **kwds) raises exc`




