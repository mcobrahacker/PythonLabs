"""
class Ticket:

    def __init__(self):
        self.arrive = {
        "105" : "Madrid",
        "211" : "London",
        "721" : "Paris",
        "429" : "New York",
        "377" : "Rome"
        }
        self.time = {
        "105" : "12:00",
        "211" : "18:30",
        "721" : "02:40",
        "429" : "10:00",
        "377" : "15:00"
        }
        self.free = {
        "105" : 12,
        "211" : 72,
        "721" : 54,
        "429" : 34,
        "377" : 57
        }
        self.tickets = {
        "105" : 5,
        "211" : 23,
        "721" : 15,
        "429" : 2,
        "377" : 14
        }

    def Counts(self):
        print("Доступные рейсы:")
        for k, v in self.arrive.items():
            print(k)


    def About_By_Arrive(self):
        name = input("Введите пункт назначения: ")

        key = ""
        for k, v in self.arrive.items():
            if v == name:
                key = k

        print(key)

        if key in self.arrive:
             if key in self.time:
                 if key in self.free:
                     if key in self.tickets:
                         print("Пункт назначения - ", name , ", номер рейса - ", key , ", кол. билетов в наличии - ", self.tickets[key] )
                         

    def About(self):
        name = input("Введите номер рейса: ")
        if name in self.arrive:
             if name in self.time:
                 if name in self.free:
                     if name in self.tickets:
                         print("Номер рейса - ", name , ", пункт назначения - ", self.arrive[name] , ", время прибытия - ", self.time[name] , ", кол. свободных мест - ", self.free[name] , ", кол. билетов в наличии -", self.tickets[name] )

    

ticket = Ticket()

def Menu():
    
    print("Выберите пункт >>> ")
    print("1 - Доступные рейсы")
    print("2 - Информация о рейсе")
    print("3 - Информация о рейсе по пункту назначения")
    print("0 - Выход из программы.")

def ChooseOption(par):


    if par == 0:
        var = 0
    elif par == 1:
        ticket.Counts()
    elif par == 2:
        ticket.About()
    elif par == 3:
        ticket.About_By_Arrive()
    else:
        print("Неправильная опция. Попробуйте другую! \n")

var = 1

while var == 1:

    Menu()
    par = int(input("Ваш выбор: "))
    if par != 0:
        ChooseOption(par)
    else:
        var = 0


"""

# Описати клас – рядок телефонної книги. Сформуйте масив записів – вашу записну телефонну
# книгу. Розробіть програму пошуку номера телефону по прізвищу і пошуку адреси по номеру
# телефону.

class Phonebook:

    def __init__(self):
        self.phones = {
        "Jack" : "666666",
        "Anna" : "777777",
        "John" : "888888",
        "Michael" : "999999",
        "Lisa" : "000000"
        }
        self.adrress = {
        "Jack" : "jack@gmail.com",
        "Anna" : "anna@gmail.com",
        "John" : "john@gmail.com",
        "Michael" : "michael@gmail.com",
        "Lisa" : "lisa@gmail.com"
        }
        self.surnames = {
        "Jack" : "Johnson",
        "Anna" : "Anderson",
        "John" : "Murray",
        "Michael" : "DeSanta",
        "Lisa" : "Collins"
        }

    def Counts(self):
        print("Доступные фамилии:")
        for k, v in self.surnames.items():
            print(v)  

    def About_Find_By_Surname(self):
        name = input("Введите фамилию: ")

        key = ""
        for k, v in self.surnames.items():
            if v == name:
                key = k

        if key in self.phones:
             if key in self.adrress:
                 if key in self.surnames:
                         print("Фамилия - ", name , ", номер телефона - ", self.phones[key] )
                         

    def About_Find_By_Email(self):
        name = input("Введите номер телефона для поиска по почте: ")

        key = ""
        for k, v in self.phones.items():
            if v == name:
                key = k

        if key in self.phones:
             if key in self.adrress:
                 if key in self.surnames:
                         print("Номер телефона - ", name , ", Почта - ", self.adrress[key] )





phonebook = Phonebook()

def Menu():
    
    print("Выберите пункт >>> ")
    print("1 - Доступные данные")
    print("2 - Поиск номера телефона по фамилии")
    print("3 - Поиск адреса по телефону")
    print("0 - Выход из программы.")

def ChooseOption(par):


    if par == 0:
        var = 0
    elif par == 1:
        phonebook.Counts()
    elif par == 2:
        phonebook.About_Find_By_Surname()
    elif par == 3:
        phonebook.About_Find_By_Email()
    else:
        print("Неправильная опция. Попробуйте другую! \n")

var = 1

while var == 1:

    Menu()
    par = int(input("Ваш выбор: "))
    if par != 0:
        ChooseOption(par)
    else:
        var = 0
       