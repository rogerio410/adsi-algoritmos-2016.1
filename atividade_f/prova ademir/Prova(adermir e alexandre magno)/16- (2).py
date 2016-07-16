def main():
	numero = input("Coloque um numero aqui: ")
	fibonacci = range(1, numero+1)
	numeroa = 1
	numerob = 1
	print "Sequencia de Fibonacci:"
	if numero == 1:
		print "0"
	else: 
		print "0"
		for i in fibonacci:
			print numeroa
			numeroc = numeroa + numerob
			numeroa = numerob
			numerob = numeroc

if __name__ == '__main__':
	main()