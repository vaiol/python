myset = {"apple", "banana", "cherry"}
# - set НЕвпорядкований 
# - set може бути змінений
# - set НЕ може містити дублікати

string_set = {"orange", "kiwi", "pineapple"}
numbers_set = {1, 5, 7, 9, 3}
boolean_set = {True, False, False}
mixed_set = {"abc", 34, True, 40, "male"}
empty_set = set()


print(type(myset))
print(len(myset))


for x in myset:
  print(x)


print("banana" in myset)

print("orange" in myset)


myset.add("orange")

print("orange" in myset)


myset.update(string_set)

myset.update(['some_fruit', 'some_other_fruit'])

# union will create new set
new_set = myset.union(boolean_set)

# remove raise error
myset.remove('some_fruit')

# discard doesn't raise error
myset.discard('some_fruit')

# спільні елементи в двої сетах
myset.intersection(string_set)


# різні елементи в двої сетах
myset.difference(string_set)


myset.pop()


myset.clear()


del myset