# -*- coding: utf-8 -*-
print "QUESTÃO N°08"
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
if A < B + C and B < A + C and C < B + A:
    perimetro = A + B + C
    print "Perimetro = %.1f" % perimetro
else:
    area = ((A+B)*C)/2
    print "Area = %.1f"%area