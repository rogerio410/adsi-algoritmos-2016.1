def main():
    print 'Mostrar os 10 primeiros multiplos de um numero'
    valor_a = input('Informe um numero: ')
    calcular_multiplo(valor_a, 1)

def calcular_multiplo(valor, ordem_multiplo):
    print valor * ordem_multiplo,
    if (ordem_multiplo < 10):
        calcular_multiplo(valor, ordem_multiplo + 1)

if __name__ == '__main__':
	main()