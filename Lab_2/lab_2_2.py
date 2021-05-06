# 2. Дано три цілих числа.
# Знайти кількість додатних чисел в початковому наборі.

# Добровольський Павло, 132 група, ФКНФМ

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print((a > 0) + (b > 0) + (c > 0))