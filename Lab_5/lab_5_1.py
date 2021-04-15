# 5. Задано список. 
# Написати програму, яка змінить матрицю таким чином,
# щоб всі елементи нижче головної діагоналі були нульовими. 


from random import randint
n = int(input('Enter size: \n')) 
d = [[randint(1, 100) for i in range(n)] for e in range(n)]
for i in range(n):
    for e in range(i):
        d[i][e] = 0
 
for i in range(n):
    print(d[i])