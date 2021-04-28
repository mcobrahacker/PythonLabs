# Описати рекурсивну функцію GCD (A, B) цілого типу, яка знаходить найбільший
# спільний дільник (НСД, greatest common divisor) двох цілих позитивних чисел A і
# B, використовуючи алгоритм Евкліда:
# НСД (A, B) = НСД (B, A mod B), B ≠ 0; НСД (A, 0) = A,
# де «mod» позначає операцію взяття залишку від ділення. За допомогою цієї
# функції знайти НСД (A, B), НCД (A, C), НCД (A, D), якщо дано числа A, B, C, D.

def GCD(A, B):
    return B if A == 0 else GCD(B % A, A)

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))

print("GCD(A, B) = ", GCD(A, B))
print("GCD(A, C) = ", GCD(A, C))
print("GCD(A, D) = ", GCD(A, D))
