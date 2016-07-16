def main():
	A0 = input("A0: ")
	Limite = input("Limite: ")
	R = input("Razao: ")
	lista(A0, Limite, R)

def lista (A, Limitea, Razao):
	resultado = 1
	for i in range(A, Limitea, Razao):
		while resultado < Limitea:
			print resultado
			resultado = resultado * Razao



if __name__ == '__main__':
	main()