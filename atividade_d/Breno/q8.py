a = input("Insira o primeiro valor: ")
b = input("Insira o segundo valor: ")
c = input("Insira o terceiro valor: ")

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
	perimetro = a + b + c
	print "Perimetro = %.1f" % perimetro
else:
	area = ((a + b) / 2) * c
	print "Area = %.1f" % area

