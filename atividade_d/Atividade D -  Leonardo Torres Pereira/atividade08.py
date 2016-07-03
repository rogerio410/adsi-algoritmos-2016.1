# -*- coding: utf-8 -*-

from math import fabs

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))


if fabs(b - c) < a < b + c or fabs(a - c) < b < a + c or fabs(a - b) < c < a + b:
	perimetro = a + b + c 
	print "Perimetro: %.1f" %  perimetro
else: 
	area_trapezio = (a + b) * c / 2
	print "Area: %.1f" % area_trapezio