
"""questao_7"""
valA = input("digite o primeiro valor: ")
valB = input("digite o segundo valor: ")
valC = input("digite o terceiro valor: ")
valD = input("digite o quarto valor: ")

if valB > valC:
	if valD > valA:
		if valC + valD > valA + valB:
			if valC > 0 and valD > 0: 
				if valA %2 == 0:
					print "valores aceitos"
				else:
					print "valores nao aceitos"
			else:
				print "valores nao aceitos"
		else:
			print "valores nao aceitos"
	else:
		print "valores nao aceitos"
else:
	print "valores nao aceitos"