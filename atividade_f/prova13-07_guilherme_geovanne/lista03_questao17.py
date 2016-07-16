# Nao ta dando a fracao resultante. So o Float.
def dezezete(numero):

	denominador = 1
	numerador = 1
	soma = 0

	for i in range(1,numero+1):
		print("{}/{}".format(numerador,denominador))
		soma += numerador/denominador
		denominador += 1

	print("%.2f" % soma)

def main():
	n = int(input("n: "))

	dezezete(n)

if __name__ == '__main__':
	main()
