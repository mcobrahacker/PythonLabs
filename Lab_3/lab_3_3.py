# 3. Визначити, чи є задане натуральне число паліндромом,
#  тобто таким, десяткова запис якого читається однаково зліва направо і справа наліво.

n = int(input("Enter N: "))
s = str(n) 
l = len(s)
for i in range(l//2):
    if s[i] != s[-1-i]: 
       print("It's not palindrome")
       break
else:
    print("It's palindrome")
