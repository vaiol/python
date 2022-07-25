
# --- Example 1

def func_if():
    num = 20
    if True:
        num = 10
    print(num)

func_if()


# --- Example 1

def func():
  num = 301
  print(num)

func()

# print(num)


# --- Example 2

def func_with_inner():
  num = 301
  def inner_func():
    print(num)
  inner_func()

func_with_inner()


# --- Example 3

GLOBAL_NUM = 300

def myfunc():
  print('GLOBAL_NUM in local scope', GLOBAL_NUM)

myfunc()

print('GLOBAL_NUM in global scope', GLOBAL_NUM)


# --- Example 4

num = 300

def myfunc():
  num = 200
  print('num in local', num)

myfunc()

print('num in global', num)

# --- Example 5

def myfunc():
  global num
  num = 300

myfunc()

print('num in global', num)
