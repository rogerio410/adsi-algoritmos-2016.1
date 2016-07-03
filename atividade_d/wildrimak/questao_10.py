numero_1, numero_2 = input("Digite um numero: "), input("Digite um numero menor que 10: ")

def tabuada_multiplicacao (numero_1, numero_2):
	print "%d x %d = %d" %(numero_1, numero_2, numero_1*numero_2)
	numero_2 = numero_2 + 1
	if numero_2 < 11:
		tabuada_multiplicacao(numero_1, numero_2)
	else:
		print "Fim."

tabuada_multiplicacao(numero_1, numero_2)
