# Описати функцію PowerA3 (A, B), яка обчислює третю степінь числа A і повертає
#її в змінній B (A - вхідний, B - вихідний параметр; обидва параметри є дійсними).
#За допомогою цієї функції знайти треті ступені п'яти даних чисел.

def PowerA3(A,B=1):
    B = A*A*A
    return B

var = 0

while var != 5:
    i = float(input("Enter a number: "))
    b = float(PowerA3(i))
    print(b)
    var = var + 1