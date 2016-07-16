limite = input("Digite o limite superior: ")
numero = input("Digite o limite inferior: ")
c = 1
p = 0
print "Primos: ",
while numero < limite:
    i = numero -1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        c += 1
    else:
        print numero
        p += 1
    numero += 1
