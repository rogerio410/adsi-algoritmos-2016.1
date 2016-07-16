def main():
	N = input("Numero: ")
	secundaria(N)

def secundaria(Numero):
	contador = 0
	resultado = 0
	for i in range(1,Numero + 1):
		if i + 1 * i + 1 <= Numero:
			resultado = i * i
			print resultado
		else:
			break

if __name__ == '__main__':
	main()