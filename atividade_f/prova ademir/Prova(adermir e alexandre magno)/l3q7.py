def main():
	N = input("Digite o numero: ")
	questao7(N)

def questao7(Numero):
	resultado = 0
	for i in range(1, Numero + 1):
		resultado = resultado + i
	print resultado

if __name__ == '__main__':
	main()