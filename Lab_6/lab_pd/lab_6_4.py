# Описати функцію Sin1 (x, ε) дійсного типу (параметри x, ε - дійсні, ε> 0),
# знаходить наближене значення функції sin (x):
# sin (x) = x - x 3 / (3!) + x 5 / (5!) - ... + (-1) n · x 2 · n + 1 / ((2 · n + 1)!) + ....
# В сумі враховувати всі складові, модуль яких більше ε. За допомогою Sin1
# знайти наближене значення синуса для даного x при шести даних ε.

import math

def Sin1(x, e):

    a = x
    y = math.sqrt(x)
    res = x
    i = 1
    while abs(a) > e:
        a = -a * y / (i + 1) / (i +2)
        res = res + a
        i = i + 2

    return res


x = float(input("Enter x -"))

var = 6
while var != 0:

    e = float(input("Enter e - "))
    print("Epsilon - ", Sin1(x,e))
    var = var -1