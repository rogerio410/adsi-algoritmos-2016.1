def main():
	Numero = input("Digite um numero: ")
	resultado = 1
	contador = Numero
	while contador > 0:
		resultado = resultado * Numero
		Numero = Numero - 1
		contador = contador - 1
	print resultado

if __name__ == '__main__':
	main()