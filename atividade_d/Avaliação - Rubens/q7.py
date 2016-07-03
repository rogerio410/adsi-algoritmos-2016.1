a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
d = int(input('digite o quarto valor: '))
soma = c + d
soma1 = a + b
if (a % 2 != 0):
	print'valores nao aceitos'
elif b > c and d > a and soma > soma1 and c > 0 and d > 0:
	print 'valores aceitos'
else:
	print 'valores nao aceitos' 