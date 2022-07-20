# tuple

mytuple = ("apple", "banana", "cherry")

mytuple_from_list = tuple(["orange", "kiwi", "banana"])

tuple3 = mytuple + mytuple_from_list
print(tuple3)

mylist_from_tuple = list(mytuple)


# frozeset

mset = {1, 2, 3, 3, 2, 1}
mlist = [1, 2, 3, 3, 2, 1]
mtuple = (1, 2, 3, 3, 2, 1)
mdict = {1: "John", 2: 23, 3: "male"}

myfrozenset1 = frozenset(mset)
myfrozenset2 = frozenset(mlist)
myfrozenset3 = frozenset(mtuple)
myfrozenset4 = frozenset(mdict)

print(myfrozenset1)
print(myfrozenset2)
print(myfrozenset3)
print(myfrozenset4)



# hash for integer unchanged
print('Hash for 252 is:', hash(252))

# hash for decimal
print('Hash for 252.21 is:', hash(252.21))

# hash for string
print('Hash for Python is:', hash('Python'))

# hash for list
# print('Hash for list is:', hash([1, 2, 3]))

# hash for tuple
# print('Hash for tuple is:', hash((1, 2, 3)))


# new_set = {[1, 2, 3], [1, 2, 3]}
# print(new_set)
