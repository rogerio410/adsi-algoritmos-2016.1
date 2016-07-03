a,b,c,d = input('Digite o valor a: '), input('Digite o valor b: '), input('Digite o valor c: '), input('Digite o valor d: ')
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
	print "Valores aceitos!"
else:
	print "Valores nao aceitos!"
