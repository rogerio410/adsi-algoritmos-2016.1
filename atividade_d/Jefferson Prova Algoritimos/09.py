def recursivo(numero, contador):
	if contador == 10:
		contador = contador + 1
	print '%d' % numero
	recursivo(numero + numero, contador)

recursivo(30, 0)
