import requests #импортируем модуль

f=open(r'volkova.pdf',"wb") #открываем файл для записи, в режиме wb

ufr = requests.get("http://pedagogy.lnu.edu.ua/departments/pedagogika/library/volkova.pdf") #делаем запрос

f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса

f.close()