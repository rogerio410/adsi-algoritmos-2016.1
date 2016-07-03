print "(Questao 8) Triangulo & Trapezio"

A = input('Valor Base maior: ')
B = input('Valor Base menor: ')
C = input('Valor Altura lado: ')

triangulo= A + B + C
trapezio = (A + B) /2 *(C)

if A < B + C:
	if B <A + C:
		if C<A+B:
			print 'E um Triangulo e o valor do perimetro eh: %d'%(triangulo)
else:
	print 'E um Trapezio e sua area eh: %d'%trapezio



