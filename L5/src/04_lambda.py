# ---- example 1

add_lambda = lambda a : a + 10
print(add_lambda(5))


# ---- example 2

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))




# ---- map without lambda

def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))








# ---- example 3

sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_answer = filter (lambda x: x > 6, sequences) 
print(list(filtered_answer))




# ---- example 4

sequences = [10, 2, 8, 7, 5, 4, 11]
squared_result = map (lambda x: x * x, sequences) 
print(list(squared_result))