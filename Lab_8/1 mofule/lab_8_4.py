# З множини чисел [1..n] виділити підмножину чисел виду p2 , де p – просте.

N = int(input("Enter N =: "))
A = set()

for i in range(2, int(N ** 0.5) + 1):
        S = 1
        while S <= N:
            A.add(pow(i, 2))
            S = S + i
print(sorted(A))


