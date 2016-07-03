def dez_multiplos(numero, indice):
	if indice == 10:
		print("FIM")
	else:
		multiplo = numero + numero*indice
		print(multiplo)
		indice = indice + 1
		dez_multiplos(numero)


def main():
	print("10 primeiros multiplos de um numero")
	numero = int(input("Insira um numero qualquer: "))
	start = int(input("tecle 0 para iniciar: ")
	dez_multiplos(numero, start)
	
if __name__ == '__main__':
	main()
