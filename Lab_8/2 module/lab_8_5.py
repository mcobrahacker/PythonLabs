# 5. Словник school містить дані про кількість учнів у десяти різних класах
# (наприклад, 1а, 1б, 2б, 6а, 7в і т.д.). Дізнайтеся скільки людей в якомусь класі. Уявіть,
# що в школі відбулися зміни, внесіть їх до словника: 1) у класі змінилася кількість учнів;
# 2) у школі з'явилося два нових класи; 3) у школі розформували один з класів. Виведіть
# вміст словника на екран.


school = {'1а':28, '1б':19, '2а':24, '2б':16, '3a':34,'3б':21, '4а': 26, "4б":31}

print(" 1 - The number of students has changed")
print(" 2 - The school has a new class")
print(" 3 - The class was disbanded at the school")
print(" 4 - Data upload")

n = int(input("Enter the operation number >>> "))
if n == 1:
  school.update({input(f"Name of the class to be changed: "): int(input(f"the number of students in class wich changed: "))})
elif n == 2:
  school.update({input(f"Class name №: "): int(input(f"the number of students in class №: "))})
elif n == 3:
  del school[input(f"Disbanded class name: ")]
elif n == 4:
  print(school)

