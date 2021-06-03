# Сформувати файл (або файли) у текстовому редакторі «Блокнот». Маємо текстовий файл
# (або файли). Варіанти:
# 1. Переписати його рядки в інший файл. Порядок розташування рядків у другому файлі
# повинен: а) збігатися з порядком рядків в заданому файлі; б) бути зворотним по
# відношенню до порядку рядків в заданому файлі.
# 

def CopyFile():
    with open('File.txt', 'r') as file2, open('File_1.txt', 'w') as file1:
        file1.writelines(file2)

def CopyFile_1():
    with open('File.txt', 'r') as readf, open('File_1.txt', 'w') as writef:
     for line in reversed(readf.readlines()):
        writef.write(line)


var = 1

def Menu():
    
    print("Виберіть опцію")
    print("1 - записати текст в інший файл без змін")
    print("2 - записати текст в інший файл починаючи з кінця")
    print("0 - вихід")

def ChooseOption(par):


    if par == 0:
        var = 0
    elif par == 1:
        CopyFile()
    elif par == 2:
        CopyFile_1()
    else:
        print("Неправильна опція! Спробуйте іншу! \n")

while var == 1:

    Menu()
    par = int(input("Ваш вибір: "))
    if par != 0:
        ChooseOption(par)
    else:
        var = 0
