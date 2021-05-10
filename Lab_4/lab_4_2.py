# Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
# Виділіть з цього рядка ім'я файлу без розширення

string_one = input("Enter a string ")
string_one.replace('/','\\')

onePos = string_one.rfind("\\")
twoPos = string_one.find('.',onePos)
extention = string_one[string_one.rfind("\\")+1 : string_one.find('.',string_one.rfind("\\"))]

print(extention)