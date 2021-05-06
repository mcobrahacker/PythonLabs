# 7. З множини чисел [1..n] виділити об’єднання підмножин - чисел виду 4k+3 і
# 5k+2.


N = int(input("Enter N: "))
A = set()
B = set()

for i in range(2, N + 1, 5):
    A.add(i)
for i in range(3, N + 1, 4):
    B.add(i)

print("Result: ", A | B)