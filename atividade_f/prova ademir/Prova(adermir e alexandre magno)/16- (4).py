def main():
	numero = input("Coloque um numero aqui (numero tem que ser maior que 2): ")
	fibonacci = range(0, numero-2)
	numeroa = 1
	numerob = 1
	print "Sequencia de Fibonacci:"
	print "0"
	print "1"
	for i in fibonacci:
		numeroc = numeroa + numerob
		numeroa = numerob
		numerob = numeroc
		print numeroa

if __name__ == '__main__':
	main()