def main():
    lado_a = float(input('Informe o valor lado a do triangulo: '))
    lado_b = float(input('Informe o valor lado b do triangulo: '))
    lado_c = float(input('Informe o valor lado c do triangulo: '))

    a_valido = abs(lado_b - lado_c) < lado_a < lado_b + lado_c
    b_valido = abs(lado_a - lado_c) < lado_b < lado_a + lado_c
    c_valido = abs(lado_a - lado_b) < lado_c < lado_a + lado_b

    if a_valido and b_valido and c_valido:
    	perimetro = lado_a + lado_b + lado_c
    	print 'Perimetro: %.1f' %(perimetro)
    else:
    	area = (lado_a + lado_b)/2 * lado_c
    	print 'Area: %.1f' %(area)


if __name__ == '__main__':
	main()