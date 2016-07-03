# -*- coding: utf-8 -*-

A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))
C = int(input("Digite o valor C: "))
D = int(input("Digite o valor D: "))

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
	print "Valores aceitos"

else: 
	print "Valores nao aceitos"

