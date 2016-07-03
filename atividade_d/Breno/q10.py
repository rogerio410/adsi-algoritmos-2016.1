def tabuada_multiplicacao(numero,multiplo):
	resultado =  numero * multiplo
	print "%dX%d = %d" % (numero,multiplo,resultado)
	multiplo += 1 
	if multiplo == 11:
		return "FIM"
	tabuada_multiplicacao(numero,multiplo)

tabuada_multiplicacao(4,1)
