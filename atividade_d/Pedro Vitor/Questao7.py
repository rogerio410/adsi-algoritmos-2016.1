valor_a = input('Digite o primeiro numero inteiro: ')
valor_b = input('\nDigite o segundo numero inteiro: ')
valor_c = input('\nDigite o terceiro numero inteiro: ')
valor_d = input('\nDigite o quarto numero inteiro: ')

soma_valor_a_b = valor_a + valor_b
soma_valor_c_d = valor_c + valor_d

if valor_b > valor_c and valor_d > valor_a and soma_valor_c_d > soma_valor_a_b and valor_c > 0 and valor_d > 0 and valor_a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

