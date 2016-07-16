def main():
	N = input("N: ")
	populacao(N)
def populacao(N):
	salario_i = 0
	filhos_i = 0
	for i in range(1,N+1):
		salario = float(input("salario: "))
		numero_filhos = float(input("numero de filhos: "))
		
		salario = salario_i+salario
		salario += salario
		
		numero_filhos = filhos_i+numero_filhos
		numero_filhos += numero_filhos

	print salario/N
	print numero_filhos/N

if __name__ == '__main__':
	main()