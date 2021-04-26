# Описати рекурсивну функцію PowerN (X, N) дійсного типу, яка знаходить
# значення N-го степеня числа X за формулами:
# X 0 = 1,
# X N = (X N / 2) 2 при парних N> 0,
# X N = X · X N-1 при непарних N> 0,
# X N = 1 / X -N при N <0
# (X ≠ 0 - дійсне число, N - ціле; у формулі для парних N повинна
# використовуватися операція цілочисельного ділення). За допомогою цієї функції
# знайти значення X N для даного X при п'яти даних значеннях N.

import math as matan

def PowerN(X, N):
    X0 = 1

    if N % 2 == 0:
        return (pow(X, N) / 2) * PowerN(X, N-1)
    elif N % 2 != 0:
        return (X * pow(X, N - 1)) * PowerN(X, N-1)
    elif N < 0:
        return (1 / X) * PowerN(X, N + 1)

var = 5

while var != 0:

    num = float(input("Enter a number: "))
    step = int(input("Enter a step: "))
    print(PowerN(num, step))
    var = var - 1
