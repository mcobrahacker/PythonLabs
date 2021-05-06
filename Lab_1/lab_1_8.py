#8. Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же цукерок.
# Добровольський Павло, 132 група, ФКНФМ

x = float(input("Enter X: "))
a = float(input("Enter cost A: "))

a = a / x

print("1 kg sweets costs: ")
print("{:10.1f}".format(a))

y = float(input("Enter Y: "))
a = a * y
print("{:10.1f}".format(y))