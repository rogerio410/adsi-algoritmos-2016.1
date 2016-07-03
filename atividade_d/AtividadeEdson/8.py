A = input("Valor A: ")
B = input("Valor B: ")
C = input("Valor C: ")
area = (((A+B)/2)*C)
perimetro = A+B+C
if A > (C-B)and A < (C+B) or B > (A-C) and B < (A+C) or C > (A-B) and C > (A+B):
	print "Perimetro %.1f"%perimetro
else:
	print "Area = %1.f"%area
	
