# 3. Визначити, чи є задане натуральне число паліндромом,
#  тобто таким, десяткова запис якого читається однаково зліва направо і справа наліво.

n = input("Enter a number ")
l = len(n)
s = ''

for i in range(1,l + 1):
    s = s + n[l-i]
if s == n:
    print("Number is polindrome")
else:
    print("Number is not polindrome")
