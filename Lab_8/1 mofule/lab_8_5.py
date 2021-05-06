# З множини чисел [1..n] виділити підмножину простих чисел p, z, таких, що
# p - z =2 (пошук “близнят”).

n = int(input("Enter N: "))
s = set()
p = 0
z = 0

def function(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n 

