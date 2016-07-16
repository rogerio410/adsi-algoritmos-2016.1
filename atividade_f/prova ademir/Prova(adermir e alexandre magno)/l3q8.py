def main():
	Numero = input("N: ")
	LimiteInferior = input("Limite Inferior: ")
	LimiteSuperior = input("Limite Superior: ")
	for i in range(LimiteInferior, LimiteSuperior + 1):
		if i % Numero == 0:
			print i

if __name__ == '__main__':
	main()