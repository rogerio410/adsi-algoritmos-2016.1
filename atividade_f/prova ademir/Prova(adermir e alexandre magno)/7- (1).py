def main():
	numero = input("Coloque um numero aqui: ")
	lista = range(numero+1)
	resultado = 0
	for i in lista:
		resultado = resultado + i
	print resultado

if __name__ == '__main__':
	main()