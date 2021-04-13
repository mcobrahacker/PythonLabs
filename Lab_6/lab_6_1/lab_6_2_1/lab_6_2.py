#Описати функцію Sign (X) цілого типу,
# яка повертає для дійсного числа X наступні значення: -1, якщо X <0; 0, якщо X = 0; 1, якщо X> 0.
# За допомогою цієї функції знайти значення виразу Sign (A) + Sign (B) для даних дійсних чисел A і B.

def Sign(X):
    if X < 0:
        return -1
    elif X == 0:
        return 0
    else:
        return 1

A = float(input("Enter A: "))
B = float(input("Enter B: "))

print(Sign(A) + Sign(B))
