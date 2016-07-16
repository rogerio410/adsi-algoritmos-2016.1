def main():
	Numero = input("N:")
	soma = 0
	cont1 = 0
	cont2 = 1
	for i in range(1, Numero + 1):
		if i % 2 != 0:
			soma+= i / float(Numero - cont1)
			cont1+= 2
		else:
			soma-= float(Numero - cont2) / i
			cont2+= 1
	print soma	

if __name__ == '__main__':
	main()