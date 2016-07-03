def multiplo(numero):
	resultado =  numero * numero
	print resultado
	if numero == 10:
		return "FIM"
	multiplo(numero + 1)

multiplo(4)