# Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# chars
a = "Hello, World!"
print(a[1])

# looping
for x in "banana":
  print(x)

# length
a = "Hello, World!"
print(len(a))

# in operator
txt = "The best things in life are free!"
print("free" in txt)

# in in if
if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)

# double quote or single quote
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
