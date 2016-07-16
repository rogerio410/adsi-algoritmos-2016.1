def main():
	Numero = input("Digite N: ")
	contador = Numero
	resultado = 0
	for i in range(1, Numero + 1):
		resultado = resultado + i
		print resultado

if __name__ == '__main__':
	main()