# Описати рекурсивну функцію Palindrome (S) логічного типу, яка повертає True,
# якщо ціле S є паліндромом (Читається однаково зліва направо і справа наліво),
# і False в іншому випадку. Оператор циклу в тілі функції не використовувати.
# Вивести значення функції Palindrome для п'яти даних чисел.

def Palindrome(S) :
   if len(S) <= 1 :
      return True
   if S[0] == S[len(S) - 1] :
      return Palindrome(S[1:len(S) - 1])
   else :
      return False

var = 5
while var != 0:
   num = input("Enter a number: ")

   var = var - 1
   if Palindrome(num):
      print("Given number is palindrome")
   else:
      print("Given number is not palindrome")