
val = '12a'

try:
    num = int(val)
    print(num)
except: # всі
    print('Some err')

try:
    num = int(val)
    print(num)
except Exception as err:  # всі
    print('Some err')

try:
    num = int(val)
    print(num)
except ValueError as err:  # тільки ValueError
    print('Some err')

# NameError
# ZeroDivisionError
# TypeError