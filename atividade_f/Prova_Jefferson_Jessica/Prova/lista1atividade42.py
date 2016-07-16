import math

def main():
    print('Informe o primeiro ponto')
    primeiro_ponto_x = int(input('Ponto X: '))
    primeiro_ponto_y = int(input('Ponto Y: '))
    print('Informe o segundo ponto')
    segundo_ponto_x = int(input('Ponto X: '))
    segundo_ponto_y = int(input('Ponto Y: '))
    distancia = math.sqrt((segundo_ponto_x - primeiro_ponto_x)**2 + (segundo_ponto_y - primeiro_ponto_x)**2)
    print('A distancia entre os dois é igual a: %.2f' % distancia)


if __name__ == '__main__':
    main()