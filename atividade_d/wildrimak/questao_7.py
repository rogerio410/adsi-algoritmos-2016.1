""" 

exemplos: 6 10 9 9 ou 6 5 4 8

"""

a, b, c, d = input("A: "), input("B: "), input("C: "), input("D: ")

if b > c:
	if d > a:
		if c + d > a + b:
			if c > 0 and d > 0:
				if a%2 == 0:
					print "Valores aceitos"
else:
	print "Valores nao aceitos"