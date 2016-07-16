def main():
	Numero = input("Digite N: ")
	resultado = 0
	contador = Numero
	while contador > 0:
		for i in range(1, Numero + 1):
			resultado = resultado + i / float(contador)
			contador = contador - 1
	print resultado

if __name__ == '__main__':
	main()