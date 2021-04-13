# Описати функцію IsPower5 (K) логічного типу, яка повертає True, якщо цілий
# параметр K (> 0) є ступенем числа 5, і False в іншому випадку. З її допомогою
# знайти кількість степенів числа 5 в наборі з 10 цілих позитивних чисел.

def IsPower5(K):

    if K < 5:
        return False
    else:
        res = 1
        i = 0 
        while res < K:
            i = i + 1
            res = res * 5
        if res == K:
            return True
        else:
            return False


var = 10
while var != 0:
    k = float(input("Enter a number: "))
    print("Result - ", IsPower5(k))
    var = var - 1