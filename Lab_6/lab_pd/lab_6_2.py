#Описати функцію TriangleP (a, h), що знаходить периметр рівнобедреного
#трикутника за його основою a і висотою h, проведеною до основи (a і h - дійсні).
#За допомогою цієї функції знайти периметри трьох трикутників, для яких дані
#основи і висоти. Для знаходження сторони b трикутника використовувати
#теорему Піфагора: b 2 = (a / 2) 2 + h 2 .

import math

def TriangleP (a, h):

    result = ((a / 2)*2 + pow(h,2))*2*3

    return result

var = 3
while var != 0:
    a = float(input("A - "))
    h = float(input("H - "))
    print("P = ", TriangleP(a,h))
    var = var - 1






