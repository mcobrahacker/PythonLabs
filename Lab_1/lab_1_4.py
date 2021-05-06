#4. Дано катети прямокутного трикутника a і b. Знайти його гіпотенузу c і периметр P: c=(a2+b2)1/2, P=a+b+c.
# Добровольський Павло, 132 група, ФКНФМ

a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = ((a ** 2) + (b ** 2)) ** (1/2)
P = a + b + c

print("c: ")
print("{:10.1f}".format(c))
print("P: ")
print("{:10.1f}".format(P))