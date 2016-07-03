a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - c) < c < (a+c):
	perimetro = a + b +c
	print 'perimetro %.2f' %(perimetro)
else:
	area = ((a + b)	/ 2) * c
	print 'area %.2f' %(area)