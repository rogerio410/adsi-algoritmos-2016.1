def main():
    print 'Tabuada de um numero'
    valor_a = input('Informe o numero para a tabuada: ')
    valor_b = input('Comecar a partir de: ')
    tabuada_multiplicacao(valor_a, valor_b)

def tabuada_multiplicacao(valor, fator):
    print '%d X %d = %d' %(valor, fator, valor * fator)
    if (fator < 10):
        tabuada_multiplicacao(valor, fator + 1)
    else:
    	print 'FIM'

if __name__ == '__main__':
	main()