# С множества чисел [1..n] выделить подмножество сложных чисел вида 6k + 1, и
# подмножество простых чисел вида 6k + 1.

n = int(input("Enter N: "))
s = set(range(n))


def function(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

s = filter(function, s)
s = filter(lambda x: (x - 1) % 6 == 0, s)

print(sorted(s))