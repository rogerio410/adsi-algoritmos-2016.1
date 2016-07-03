print '(Questao 7) Leitura de 4 numeros'

A= int(input('>> Digite o valor do Primeiro Valor: '))
B= int(input('>> Digite o valor do Segundo Valor: '))
C= int(input('>> Digite o valor do Terceiro Valor: '))
D= int(input('>> Digite o valor do Quarto Valor: '))

if B>C and D>A and C+D > A+B:
		if A > 0:
			if C > 0:
				print "VALORES ACEITOS"
else:
	print 'VALORES NAO ACEITOS'