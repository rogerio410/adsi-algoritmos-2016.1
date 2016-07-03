## Mariano Barbosa de Carvalho Neto
def tabuada(num1,num2):
	if num2 < 10:
		mult2 = num1*(num2 - 1)
		mult1 = num1*tabuada(num1,num2)
		return mult1
	elif num2 == 10:
		return "FIM"

def main():
	num1 = input("digite um numero a ser tabulado: ")
	num2 = input("digite o inicio da sequencia: ")
	tabuada(num1,num2)
	tabulacao = tabuada(num1,num2)
	print tabulacao
main()