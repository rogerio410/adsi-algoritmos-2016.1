def tabuada(numero,multiplicador):
	valor = numero * multiplicador
	print '%d x %d = %d' %(numero,multiplicador,valor)
	if multiplicador < 10 and multiplicador > 0:
		multiplicador = multiplicador + 1
		tabuada(numero,multiplicador)
	else:
		print 'FIM'
numero = input('Digite um numero: ')
multiplicador = input('Digite um numero para dar inicio a tabuada!: ')
tabuada(numero,multiplicador)
