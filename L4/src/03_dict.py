car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# - dict впорядкований 
# - dict може бути змінений
# - dict НЕ може містити дублікати

empty_dict = dict()




new_car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2022,
  "electric": True,
  "colors": ["red", "white", "blue"],
  "features": {
    "bluetooth": True,
    "AWD": False,
  }
}

print('New MUSTANG: Electric', new_car_dict["electric"])

print('New MUSTANG: Basic color', new_car_dict.get("colors")[0])

print('New MUSTANG: AWD', new_car_dict["features"]['AWD'])

print('New MUSTANG: Bluetooth', new_car_dict.get("features").get('AWD'))

# отримуємо список ключів
new_car_keys = new_car_dict.keys()

print('New mustang keys', new_car_keys) # перед зміною ключів

# додаємо новий ключ
new_car_dict["release_date"] = "2022-01-01"

# оновлюємо значення
new_car_dict.update({"year": 2020})

print('New mustang keys', new_car_keys) # після зміни ключів



# отримуємо список значень
new_car_values = new_car_dict.values()

# отримуємо список всіх елементів
new_car_values = new_car_dict.items()

if 'release_date' in new_car_dict:
    print('New car has relase date which is', new_car_dict.get('new_car_dict'))


for key in new_car_dict:
  print(new_car_dict[key])

for key in new_car_dict.keys():
  print(new_car_dict[key])

for value in new_car_dict.values():
  print(value)

for key, value in new_car_dict.items():
  print(key, value)





# видалення елментів
new_car_dict.pop('release_date')

del new_car_dict['electric']


# очешення dict
new_car_dict.clear()

# видалення dict
del new_car_dict
