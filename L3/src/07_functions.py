def hello_func():
    print("Hello from a function")


def my_func(who, count = 1):
    res = []
    for _ in range(count): # 0, 1, 2, 3, 4
        res.append(f'Hello {who}')

    return res
    

print('Це не в функції')


my_func('everyone', 5) # ['Hello everyone', ...]

alex_greetings = my_func('Alex')
print(alex_greetings)

print(my_func('ITNATION', 3))

# parameters vs arguments
# *args
# number of args
# keyword args
# default parameter val

# return values
