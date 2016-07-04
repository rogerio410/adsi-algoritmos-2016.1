#7 question
#29/06 - jhonatan matheus
#dados validos A = 2, B = 4, C = 3, D = 6
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

if((B > C)and(D > A)and(C + D > A + B)and(C + D > 0)and(A % 2 == 0)):
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
