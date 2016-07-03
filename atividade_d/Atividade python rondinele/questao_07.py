def main():
    valor_a = input('Informe o valor a: ')
    valor_b = input('Informe o valor b: ')
    valor_c = input('Informe o valor c: ')
    valor_d = input('Informe o valor d: ')

    soma_c_d = valor_c + valor_d
    soma_a_b = valor_a + valor_b
    positivo_c = valor_c > 0
    positivo_d = valor_d > 0
    a_par = valor_a % 2 == 0
    if valor_b > valor_c and valor_d > valor_a and soma_c_d > soma_a_b and positivo_c and positivo_d and a_par:
        print 'Valores aceitos'
    else:
        print 'Valores nao aceitos'

if __name__ == '__main__':
	main()