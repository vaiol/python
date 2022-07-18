print('Введіть кількість яблук в магазині')
apples_in_store = input()
print('Введіть кількість яблук у вас')
apples_with_me = input()

if apples_with_me > apples_in_store:
  print("Я маю більше яблук ніж в магазині!")
elif apples_with_me == apples_in_store:
  print("Я маю стільки ж яблук як і в магазині!")
else:
  print("Магазин має більше яблук!")


# яка тут помилка?)