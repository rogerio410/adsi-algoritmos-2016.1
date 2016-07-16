def main():
	inicio = input("A0: ")
	limite = input("Limite: ")
	r = input("R: ")
	P_G(A0,limite,r)

def P_G(inicio,limite,r):
	for i in range(inicio,limite+1,r):
			print inicio*(r**limite)

if __name__ == '__main__':
	main()
