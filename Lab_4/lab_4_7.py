# 7. Дано рядок. Розріжте його на дві рівні частини
# (якщо довжина рядка - парна, а якщо довжина рядка непарна,
# то довжина першої частини повинна бути на один символ більше).
# Переставте ці дві частини місцями,
# результат запишіть в новий рядок і виведіть на екран.

str = input("Enter string ")

if len(str) % 2 != 0: 
    print(str[(len(str)) // 2:] + str[:len(str) // 2])
else:
    print(str[(len(str)) +1 // 2:] + str[:len(str) // 2])

