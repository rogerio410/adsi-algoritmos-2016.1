def main():
	nota1 = float(input("insira primeira nota: "))
	nota2 = float(input("insira segunda nota: "))
	media(nota1,nota2)

def media(nota1,nota2):
	media = (nota1+nota2)/2
	if media >= 7.0:
		if media == 10:
			print "APROVADO COM DISTINCAO"
		else:
			print"APROVADO"
	else:
		print"REPROVADO"	

if __name__ == '__main__':
	main()
