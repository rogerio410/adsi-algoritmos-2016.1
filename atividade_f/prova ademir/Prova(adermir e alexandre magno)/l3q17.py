def main():
	Numero = input("Digite N: ")
	resultado = 0
	for i in range(1, Numero + 1):
		resultado = resultado + 1/float(i)
	print resultado

if __name__ == '__main__':
	main()