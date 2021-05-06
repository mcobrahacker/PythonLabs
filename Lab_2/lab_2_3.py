# 3. Дано три числа. Знайти суму двох найбільших з них.

# Добровольський Павло, 132 група, ФКНФМ

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a<b:
    min = a
else:
    min = b
if c<min:
    min = c
n = a+b+c-min
print("The sum of the two largest numbers are: ", n)