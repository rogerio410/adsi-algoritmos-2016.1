def main():
	Numero = input("Digite a quantidade de numeros que voce ira digitar: ")
	contador = Numero
	numerob = 0
	while contador > 0:
		Numeroa = input("Digite o numero: ")
		if Numeroa > numerob:
			numerob = Numeroa
		contador = contador - 1
	print numerob

if __name__ == '__main__':
	main()