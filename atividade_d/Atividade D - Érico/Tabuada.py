def calculadora(numero, multiplicador):
	if multiplicador > 10:
		print("FIM.")
	else: 
		resultado = numero * multiplicador
		print ("%d X %d = %d"%(numero, multiplicador, resultado))
		multiplicador = multiplicador + 1
		calculadora(numero, multiplicador)

def main():
	print("Calculadora")
	numero = int(input("Insira o numero a ser calculado: "))
	multiplicador = int(input("A partir de que numero ele sera multiplicado: "))
	calculadora(numero, multiplicador)

if __name__ == '__main__':
	main()