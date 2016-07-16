def main():
	LimiteInferior = input("Limite Inferior: ")
	LimiteSuperior = input("Limite Superior: ")
	for i in range(LimiteInferior, LimiteSuperior + 1):
		if i % 2 == 0:
			print i

if __name__ == '__main__':
	main()