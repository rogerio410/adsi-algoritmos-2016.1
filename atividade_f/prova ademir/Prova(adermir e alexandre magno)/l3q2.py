def main():
	print "Um programa para ler N e escrever todos os numeros pares entre 1 a N"
	Numero = input("Digite N: ")
	for i in range(2, Numero + 1, 2):
		print i

if __name__ == '__main__':
	main()