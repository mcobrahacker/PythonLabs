# Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
# Виділіть з цього рядка ім'я файлу без розширення

string_one = input("Enter a string ")

onePos = string_one.rfind('/')
print(onePos)
twoPos = string_one.find('.',onePos)
print(twoPos)
extention = string_one[onePos+1 : twoPos]
print(extention)
