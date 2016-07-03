print "Programa para determinar se sao numeros aceitos ou nao."
A = input("Digite o primeiro numero:")
B = input("Digite o segundo numero:")
C = input("Digite o terceiro numero:")
D = input("Digite o quarto numero:") 
if B > C and D > A and C+D>A+B and C > 0 and D > 0 and A%2 == 0:
	print "Valores aceitos"
else: 
	print "Valores nao aceitos"