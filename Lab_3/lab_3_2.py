# 2. Визначити, чи є задане натуральне число досконалим, тобто рівним сумі всіх своїх дільників,
# крім самого цього числа (наприклад, число 6 досконале: 6 = 1 + 2 + 3).

a = int(input("Enter a number >>> "))

def Perfect(n):
        s = [j for j in range(1, n // 2 + 1) if not n % j]
        return sum(s) == n

print(Perfect(a))
