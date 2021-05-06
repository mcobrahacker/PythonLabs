#Дано рядки S, S1 і S2. Замінити в рядку S останнє входження рядка S1 на рядок S2.

S = input("S: ")
S1 = input("S1: ")
S2 = input("S2: ")

var = S.rfind(S1)

if var != -1:
    print(S[:var] + S2 + ' ' + S[var:])