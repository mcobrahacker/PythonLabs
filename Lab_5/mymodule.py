# Python Module for main app

# Розробіть функції для здійснення наступних операцій зі списками:
# 1. Введення списку;
# 2. Заповнення списку випадковими числами;
# 3. Виведення списку;
# 4. Пошук елементу за значенням;
# 5. Пошук максимального елементу;
# 6. Сортування списку за зростанням (спаданням);
# 7. Пошук середнього арифметичного;


import random

def inputList():
    """ Input list """
    a = list(input("Enter list elements - ").split())
    return a



def generateNums(var):
    """ Filling the list with random numbers """

    min = int(input("Min - "))
    max = int(input("Max - "))
    var1 = list(range(min, max))
    var.extend(var1)
    return var


def outputList(var):
    """ Output list """
    print(var)



def itemSearch(var):
    """ Find an element by value """
    indexSearch = input("Enter item name - ")
    print(var.index(indexSearch))


def maxElementSearch(var):
    """ Find max element in list """
    maximum = var[0]
    for i in range(1, len(var)):
        if var[i] > maximum:
            maximum = var[i]
    print(maximum)


def sortByLowerValue(var):
    """ Sort by lower value """
    print(recompile(var).sort())


def sortByHigherValue(var):
    """ Sort by higher value """
    print(recompile(var).sort(reverse = True))

def recompile(var):
    for i in range(0, len(var)):
        var[i] = int(var[i])
    return var

def average(var):
    """ Search for average of nums """

    print(float(sum(recompile(var))) / max(len(var), 1))