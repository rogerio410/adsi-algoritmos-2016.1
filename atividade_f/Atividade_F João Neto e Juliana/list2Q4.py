# Questao da Lista Errada
def main():
	ler_numero()



def ler_numero():
	numero = input("Digite um numero de dois digitos:")
	dezena = (numero%100)/10
	unidade = numero%10
	if dezena == unidade:
		print "O algarismo da dezena eh igual o da unidade %d,%d" %(dezena, unidade)
	else:
		print"Os algarismos sao diferentes %d,%d" %(dezena, unidade)





if __name__ == '__main__':
    main()