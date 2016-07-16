# nao fez recursivo. E Era para imprimir N elementos e nao Limite N.

#number = input("Insira o Valor: ")
def fibonaci(limite):
	a = 1
	b = 1
	atual = a + b
	print a
	print b
	while atual <= limite:
		print atual
		a = b
		b = atual
		atual = a + b

def main():
	limite = input("Insira o limite:")
	fibonaci(limite)
if __name__ == '__main__':
	main()