def main():
	inicio = input('Insira um valor inicial:\n')
	quantidade_de_vezes = input('Insira o numero de vezes:\n')
	razao= input('Digite a razao:\n')
	progressao_geometrica(inicio, quantidade_de_vezes, razao)

def progressao_geometrica(inicio, quantidade_de_vezes, razao):
	cont = 0
	while cont < quantidade_de_vezes:
		inicio = inicio * razao
		cont+= 1
		print inicio,

if __name__ == '__main__':
	main()