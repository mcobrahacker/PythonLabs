#Завдання 1.
#Створіть файли, у яких будуть міститися рядки з іменами студентів та їх середніми балами.
#Реалізуйте читання файлів, запис та дозапис у файли, пошук файлів у каталозі та пошук
#даних у файлі. Також реалізуйте сортування даних у файлі за середнім балом.

def ReadFile():
    fhand = open('Students.txt')
    inp = fhand.read()
    b = len(inp)
    print(inp[:b])

def AddLine():
    i = input("Введіть 5 пробілів перед оцінкою, а потім введіть 8 пробілів перед іменем студента: ")
    with open('Students.txt', 'a') as file1: 
         file1.writelines(i) whi

def WriteFile():
    fout = open('Students.txt', 'w')
    i = input("Введіть оінку, потім ім’я студента: ")
    fout.write(i)

def SortMark():
    with open("Students.txt", "r+") as f:

        lines = f.readlines()
        lines.sort(reverse=True)        
        f.seek(0)
        f.writelines(lines)

def SeeFile():
    A = input("Вивести новий список студентів? (Так / Ні)")
    while(A != "Так" and A != "Ні"):
        print("Виберіть (Так) чи (Ні)")
        A = input("Вивести новий список студентів? (Так / Ні)")
    if(A == "Так"):
        ReadFile()

def File1():
    with open('Students_1.txt', 'r') as file2, open('Students.txt', 'w') as file1:
        file1.writelines(file2)
        
File1()

var = 1

def Menu():
    
    print("Виберіть опцію")
    print("1 - зчитати файл")
    print("2 - записати файл")
    print("3 - дозапис файлу")
    print("0 - закінчити роботу")


def ChooseOption(par):


    if par == 0:
        var = 0
    elif par == 1:
        ReadFile()
    elif par == 2:
        WriteFile()
        SeeFile()
    elif par == 3:
        AddLine()
        SeeFile()
    else:
        print("Неправильна опція! Спробуйте іншу! \n")

while var == 1:

    Menu()
    par = int(input("Ваш вибір: "))
    if par != 0:
        ChooseOption(par)
    else:
        var = 0



