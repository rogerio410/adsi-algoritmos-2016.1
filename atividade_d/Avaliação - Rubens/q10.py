def numero(num1, num2):
	if num2 > 10:
		print 'fim'
	else:
		calculo = num1 * num2
		print 'num * num2 %d' %(calculo)
		numero (num1, num2 + 1)

if __name__ == '__main__':
	num1 = int(input('digite o primeiro numero: '))
	num2 = int(input('digite o segundo numero: '))
	numero(num1, num2)		

