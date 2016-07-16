# Imprimindo 1 elemento a mais.
def main():
	valor_n = input('Digite um valor para sequiencia: ')
	fibonacci = 1
	numero_anterior = 0
	print '0'
	sequencia(valor_n,fibonacci,numero_anterior)

def sequencia(valor_n,fibonacci,numero_anterior):
	if valor_n == 0:
		print'fim'
	else:
		print fibonacci
		fibonacci += numero_anterior
		numero_anterior = fibonacci - numero_anterior
		sequencia(valor_n - 1,fibonacci,numero_anterior)
if __name__ == '__main__':
	main()