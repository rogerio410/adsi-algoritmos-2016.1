def main():
	Numero = input("Digite a quantidade de numeros que voce ira digitar: ")
	contador = Numero
	soma = 0
	while contador > 0:
		Numeroa = input("Digite o numero: ")
		soma = soma + Numeroa
		contador = contador - 1
	media = soma / Numero
	print "Soma: %i" %soma
	print "Media: %i" %media

if __name__ == '__main__':
	main()