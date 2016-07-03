def multiplos(numero1, numero2):
	if numero2 > 10:
		print 'fim'
	else:
		calculo = numero1 * numero2
		print 'mutiplo sera %d' %(calculo)
		multiplos(numero1, numero2 + 1)

if __name__ == '__main__':
	numero1 = int(input('digite o primeiro numero: '))
	numero2 = 1
	multiplos(numero1, numero2)	