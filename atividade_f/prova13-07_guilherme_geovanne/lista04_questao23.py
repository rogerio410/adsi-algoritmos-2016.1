# E para imprimir o N Elementos/Termos e nao Limitado a um valor

valor = 0
inicio = 1
limite = 20
razao = 2

#questao 4
def progressao_geometrica(inicio,limite,razao):
    valor = inicio
    posicao = 1

    while valor < limite:
        print valor
        valor = inicio * pow(razao,posicao)
        posicao += 1

# progressao_geometrica(1,20,2)
def main():
	inicio = int(input(""))
	limite = int(input(""))
	razao  = int(input(""))
	progressao_geometrica(inicio,limite,razao)


if __name__ == '__main__':
	main()
