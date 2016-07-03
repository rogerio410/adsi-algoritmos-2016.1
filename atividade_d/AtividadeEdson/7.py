A = int(input("Valor A: "))
B = int(input("Valor B: "))
C = int(input("Valor C: "))
D = int(input("Valor D: "))
if (B > C) and (D > A) and (C+D) > (A+B) and (C>0) and (D>0) and (A%2==0):
	print "Valores aceitos"
else:
	print "Valores nao aceitos" 
