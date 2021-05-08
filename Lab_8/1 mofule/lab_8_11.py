# С множества чисел [1..n] выделить подмножество сложных чисел вида 6k + 1, и
# подмножество простых чисел вида 6k + 1.

N = int(input("Enter N: "))
print("\n")

prime = set()
hard = set()
m = set()

for i in range(2, N):
    m.add(i)

for i in range(N):
    prime.add(6 * i + 1)

for i in m:
    if i in prime:
        hard.add(i)

print("Numbers - ", sorted(m))
print("\n")
print("Prime result - ",sorted(prime))
print("\n")
print("Hard result - ", sorted(hard))