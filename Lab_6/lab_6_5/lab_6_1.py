# Описати функцію RectPS (x1, y1, x2, y2, P, S), яка обчислює периметр P і площу
#S прямокутника зі сторонами, паралельними осям координат, за координатами
#(x1, y1), (x2, y2) його протилежних вершин (x1, y1, x2, y2 - вхідні, P і S - вихідні
#параметри дійсного типу). За допомогою цієї функції знайти периметри і площі
#трьох прямокутників з даними протилежними вершинами.

import math

def RectPS(x1, y1, y2, x2, P=0, S=0):
    
    P = (abs(x2-x1) + abs(y2-y1)) * 2
    S = (abs(x2-x1) * abs(y2-y1))
    return P, S

x1 = float(input("Enter a number: "))
x2 = float(input("Enter a number: "))
y1 = float(input("Enter a number: "))
y2 = float(input("Enter a number: "))

result = RectPS(x1,y1,x2,y2)

print("P = ", result[0])
print("S = ", result[1])


