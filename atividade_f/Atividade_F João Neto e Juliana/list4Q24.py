#Errada
def main():
	x_inicial  = input("Digite o termo inicial da PA:")
	n_quantidade = input("Digite quantos termos tem a PA")
	razao = input("Digite a razao da PA:")
	Pa = x_inicial + x_inicial * (n_quantidade-1)
	for i in range(x_inicial, Pa, razao):
		print i


if __name__ == '__main__':
	main()