# Nao foi recursiva.

def main():
	N = input("N: ")
	fibonacci(N)
def fibonacci(N):
	while N < 2:
		N = input("Digite numero maior ou igual a 2: ")
	else:
		n1=0
		n2=1
		print n1,n2,
		for i in range(N - 2):
			atual = n1+n2
			n1 = n2
			n2 = atual
			print  atual,

if __name__ == '__main__':
	main()