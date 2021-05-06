# 10. Дано ціле число N (> 0).
#  Знайти значення виразу 1.1 - 1.2 + 1.3 - ...
#  (N доданків, знаки чергуються).
#  Умовний оператор не використовувати

import random

N = input("Enter a number ")

print("N = ", N)

S = 0.0

for i in range(1,N+1):
    x = 2 * i - 1
    S = S + x
    print(i ," : ", x ," : ", S)

print("Sum = ", S)
						