valor_a = input('Digite o primeiro valor real: ')
valor_b = input('\nDigite o segundo valor real: ')
valor_c = input('\nDigite o terceiro valor real: ')

diferenca_lados_b_c = valor_b - valor_c
soma_lados_b_c = valor_b + valor_c
diferenca_lados_a_c = valor_a - valor_c
soma_lados_a_c = valor_a + valor_c
diferenca_lados_b_c = valor_b - valor_c
soma_lados_a_b = valor_a + valor_b

if valor_a > diferenca_lados_b_c and valor_a < soma_lados_b_c:
    if valor_b > diferenca_lados_a_c and valor_b < soma_lados_a_c:
        if valor_c > diferenca_lados_b_c and valor_c < soma_lados_b_c:
            perimetro_triangulo = valor_a + valor_b + valor_c
            print('\nO perimetro do triangulo eh %.1f') % perimetro_triangulo
else:
    area_trapezio = (valor_a + valor_b) / 2 * valor_c
    print('\nA area do trapezio eh %.1f') % area_trapezio

#1 2 4
 
            

    



