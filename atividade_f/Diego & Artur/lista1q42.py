from math import sqrt
def main():
	ponto_x1 = input('Insira o valor da posicao X1: ')
	ponto_x2 = input('Insira o valor da posicao X2: ')
	ponto_y1 = input('Insira o valor da posicao Y1: ')
	ponto_y2 = input('Insira o valor da posicao Y2: ')
	distancia_entre_pontos(ponto_x1, ponto_x2, ponto_y1, ponto_y2)

def distancia_entre_pontos(ponto_x1, ponto_x2, ponto_y1, ponto_y2):
	distancia = sqrt(((ponto_x1 - ponto_x2)**2)+((ponto_y1-ponto_y2)**2))
	print 'A distancia entre os pontos e %.2f' %(distancia)

if __name__ == '__main__':
	main()