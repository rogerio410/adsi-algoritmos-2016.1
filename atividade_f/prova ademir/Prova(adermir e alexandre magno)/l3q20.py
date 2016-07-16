def main():
	Numero = input("N:")
	soma = 0
	for i in range(1, Numero + 1):
		if i % 2 != 0:
			soma+= 1 / float(i)
		else:
			soma-= 1/ float(i)
	print soma	

if __name__ == '__main__':
	main()