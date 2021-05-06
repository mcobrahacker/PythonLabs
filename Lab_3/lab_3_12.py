# 12. Дано дійсне число - ціна 1 кг цукерок.
# Вивести вартість 1, 2, ..., 10 кг цукерок.

price = float(input("Enter a price "))

for i in range(1, 11):
  print(price * i)
