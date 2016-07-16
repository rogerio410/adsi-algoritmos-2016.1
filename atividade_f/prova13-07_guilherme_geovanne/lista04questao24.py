# E para imprimir o N Elementos/Termos e nao Limitado a um valor

def pa(inicio,limite,razao):

	for i in range(inicio,limite+1,razao):
		print (i)


def main():
	inicio, limite , razao  = int(input("")),int(input("")),int(input(""))
	pa(inicio,limite,razao)

if __name__ == '__main__':
	main()
