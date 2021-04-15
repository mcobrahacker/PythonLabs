# Реалізуйте програму, яка використовує всі функції зі створеного модуля. Зробіть описи Doc strings для кожної реалізованої функції.

import mymodule as module

while True:
    print("1. Введення списку")
    print("2. Заповнення списку випадковими числами")
    print("3. Виведення списку")
    print("4. Пошук елементу за значенням")
    print("5. Пошук максимального елементу")
    print("6. Сортування списку за зростанням")
    print("7. Сортування списку за спаданням")
    print("8. Пошук середнього арифметичного")
    print("0. Вихiд iз програми")

    cmd = input("Виберiть пункт: ")

    if cmd == "1":
        module.inputList()

    elif cmd == "2":
        var = module.inputList()
        print(module.generateNums(var))

    elif cmd == "3":
        var = module.inputList()
        module.outputList(var)

    elif cmd == "4":
        var = module.inputList()
        module.itemSearch(var)

    elif cmd == "5":
        var = module.inputList()
        module.maxElementSearch(var)

    elif cmd == "6":
        var = module.inputList()
        module.sortByHigherValue(var)

    elif cmd == "7":
        var = module.inputList()
        module.sortByLowerValue(var)

    elif cmd == "8":
        var = module.inputList()
        module.average(var)

    elif cmd == "0":
        break

    else:
        print("Ви ввели неправильне значення")
