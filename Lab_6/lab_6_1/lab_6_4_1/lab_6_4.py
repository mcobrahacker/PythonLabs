# Описати функцію Power1 (A, B) дійсного типу, яка знаходить величину AB за формулою AB = exp (B · ln (A)) (параметри A і B - дійсні).
# У разі нульового або негативного параметра A функція повертає 0.
# З допомогою цієї функції знайти степені AP, BP, CP, якщо дано числа P, A, B, C.

import math as mat

def Power1(A, B):

    if A == 0 or A < 0:
        return 0;
    else:
        return mat.exp(B * mat.log10(A))

P = float(input("Enter P: "))
A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))

print(Power1(A, P))
print(Power1(B, P))
print(Power1(C, P))
