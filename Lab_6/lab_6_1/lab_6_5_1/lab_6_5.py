# Описати функцію Calc (A, B, Op) дійсного типу, що виконує над ненульовими дійсними числами A та B одну з арифметичних операцій і повертає її результат.
# Вид операції визначається цілим параметром Op: 1 - віднімання, 2 - множення, 3 - ділення, інші значення - додавання.
# За допомогою Calc виконати для даних A і B операції, які визначаються даними цілими N1, N2, N3.

def Calc(A, B, Op):
    if Op == 1:
        return A - B
    elif Op == 2:
        return A * B
    elif Op == 3:
        return A / B
    else:
        return A + B

N1 = int(input("Enter a first number: "))
N2 = int(input("Enter a second number: "))
N3 = int(input("Enter a Op: "))

print(Calc(N1, N2, N3))
