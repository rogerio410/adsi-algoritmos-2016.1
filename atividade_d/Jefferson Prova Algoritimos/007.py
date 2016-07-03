numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))
numero3 = int(input('Informe o terceiro numero: '))
numero4 = int(input('Informe o quarto numero: '))

if numero2 > numero3 and numero4 > numero1 and numero3 + numero4 > numero1 + numero2 and numero3 >= 0 and numero4 >= 0 and numero1%2 == 0:
	print('Valores aceito')
else:
	print('Valores não aceitos')