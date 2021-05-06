# Описати рекурсивну функцію Combin1 (N, K) цілого типу, яка знаходить C (N, K)
# - число поєднань з N елементів по K - за допомогою рекурентного
# співвідношення:
# C (N, 0) = C (N, N) = 1,
# C (N, K) = C (N - 1, K) + C (N - 1, K - 1) при 0 <K <N.

def Combin1(N, K):
    if K == 0:
        return 1
    elif N == K:
        return 1
    else:
        return Combin1(N-1,K) + Combin1(N-1,K-1)
    
N = int(input("Enter N - "))

var = 5
while var != 0:
    K = int(input("Enter K - "))
    print(Combin1(N,K))
    var = var - 1