#coding: utf-8

def escreva_multiplos(numero, indice):
	if indice>10:
		print("Terminado!")
	else:
		print(numero*indice)
		escreva_multiplos(numero, indice+1)
	


def main():
	numero = int(input("Digite um Número: "))
	print("Os 10 primeiros múltiplos são: \n",escreva_multiplos(numero,1))

if __name__ == "__main__":
	main()
