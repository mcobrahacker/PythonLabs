# 1. З множини чисел [1..n] виділити підмножину простих чисел виду 4k+1


n = int(input("Enter N: "))
s = set(range(n))


def function(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

s = filter(function, s)
s = filter(lambda x: (x - 1) % 4 == 0, s)

print(sorted(s))