
def main():
	A = int(input('insira o valor de A'))
	B = int(input('insira o valor de B'))
	C = int(input('insira o valor de C'))
	D = int(input('insira o valor de D'))
	if(B > C):
		if(D > A):
			if(C+D)>(A+B):
				if (C>0 and D>0):
					if(A%2 == 0):
						print('valores aceitos')
						return

	print('Valores nao aceitos')
if __name__ == '__main__':
	main()