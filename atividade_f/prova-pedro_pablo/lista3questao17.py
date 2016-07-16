def caucular(numero):
	soma = 0.0
	for x in range(1,numero+1,1):
		print('%.2f ') %(soma)
		soma =  soma + (1 / float(x))
	print "Valor em float {} ".format(soma)

def main():
	numero = input("Digite um numero: ")
	caucular(numero)

if __name__ == '__main__':
	main()