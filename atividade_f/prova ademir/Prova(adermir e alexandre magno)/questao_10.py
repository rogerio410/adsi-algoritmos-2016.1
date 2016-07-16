def limites():
	limite_sup = input("Digite o numero superior: ")
	limite_inf = input("Digite o numero inferior: ")
	inicio = limite_inf + 1
	termino = limite_sup + 1
	if inicio % 2 == 0:
		inicio = inicio - 1
		numeros = range (inicio,termino,2)
		print numeros		
	else: 
		numeros = range (inicio,termino,2)
		print numeros
if __name__ == "__main__":
	limites()