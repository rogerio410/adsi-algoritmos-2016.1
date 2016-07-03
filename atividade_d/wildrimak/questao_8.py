import math

a, b, c = input("Lado A: "), input("Lado B: "), input("Lado C: ")



if math.fabs(b - c) < a and a < b + c:
	if math.fabs(a - c) < b and b < a + c:
		if math.fabs(a - b) < c and c < a + b:
			perimetro = a + b + c
			print "Perimetro = %.1f" %(perimetro)
else:
	area_trapezio = ((a + b) / 2) * c
	print "Area = %.1f" %(area_trapezio)
