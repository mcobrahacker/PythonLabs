# 1. Описати програму з використанням словника, у якій зберігаються дані про
# товари, їх кількість та ціну.


dict_count = {
    "Молоко" : 100,
    "Сир" : 100,
    "Творіг" : 100,
    "Ковбаска" : 100,
    "Перчик" : 100
}

dict_price = {
    "Молоко" : 10,
    "Сир" : 10,
    "Творіг" : 10,
    "Ковбаска" : 10,
    "Перчик" : 10
}

def Find_Item_Name():
    name = input("Введіть ім'я - ")
    if name in dict_count:
        if name in dict_price:
            print(name, ", ціна - ", dict_price[name], ", кол. - ", dict_count[name])

def Find_Item_Price():
    name = input("Введіть ім'я - ")
    if name in dict_count:
        if name in dict_price:
            print(name, ", ціна - ", dict_price[name])

def Find_Item_Count():
    name = input("Введіть ім'я - ")
    if name in dict_count:
        if name in dict_price:
            print(name, ", кол. - ", dict_count[name])

def Menu():
    
    print("Виберіть опцію")
    print("1 - Знайти товар за назвою")
    print("2 - Дізнатися ціну товару")
    print("3 - Дізнатися кількість товару")
    print("0 - вихід")

def ChooseOption(par):


    if par == 0:
        var = 0
    elif par == 1:
        Find_Item_Name()
    elif par == 2:
        Find_Item_Price()
    elif par == 3:
        Find_Item_Count()
    else:
        print("Неправильна опція! Спробуйте іншу! \n")

var = 1

while var == 1:

    Menu()
    par = int(input("Ваш вибір: "))
    if par != 0:
        ChooseOption(par)
    else:
        var = 0
