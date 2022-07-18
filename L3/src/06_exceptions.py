
val = '12q'

try:
    num = int(val)
    if num == 13:
        raise Exception('really bad value')
    print(num)
except Exception as err:
    print('Some err', err)

# NameError
# ZeroDivisionError
# TypeError