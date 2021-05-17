# 3.Описати програму з використанням словника. В одному рядочку введено текст.
# Слова відділяються одним або кількома пробілами або символом кінця рядка.
# Для кожного слова підрахувати кількість входжень у текст (частотний словник).
# Після додавання або вилучення слова вносити відповідні зміни у словник.

text = input('Enter: ')

lst = text.split()
d = {i: lst.count(i) for i in lst}
print(d)

while True:
    print("1. Add word")
    print("2. Delete word")
    a = int(input("Choose option: "))

    if a == 1:
        text = input('Input text: ')
        lst = text.split()
        for k in lst:
            if not k in d:
                d[k] = 0
            d[k] += 1
        print(d)
    if a == 2:
        text = input('Input text: ')
        lst = text.split()
        for k in lst:
            if not k in d:
                continue
            d[k] -= 1
            if d[k] == 0:
                d.pop(k)
        print(d)

