def multiplica(numero,contador):
	valor = numero * contador
	print valor
	if contador < 10 and contador > 0:
		contador = contador + 1
		multiplica(numero,contador)
numero = input('Digite um numero inteiro: ')
multiplica(numero,1)
