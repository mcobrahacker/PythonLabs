#5. Дано ціле число.
# Вивести його рядок-опис виду «від'ємне парне число»,
# «нульове число», «додатне непарне число» і т. д.

# Добровольський Павло, 132 група, ФКНФМ

a = int(input("Введите любое число: "))
if a==0:
    print("Число нулевое.")
elif a>0:
    print("Число положительное.")
elif a<0:
    print("Число отрицательное.")
elif ((a%2)==0):
    print("Число чётное.")
elif ((a%2)==1):
    print("Число нечётное.")