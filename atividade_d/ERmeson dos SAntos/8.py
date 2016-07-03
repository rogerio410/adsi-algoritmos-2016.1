print "Progama para ler 3 valores reais (A, B e C) e verificar se eles formam ou nao um triangulo."
ladoa = input ("Coloque o primeiro valor:")
ladob = input ("Coloque o segundo valor:")
ladoc = input ("Coloque o terceiro valor:")
if ladob - ladoc < ladoa and ladob + ladoc > ladoa and ladoa - ladoc < ladob < ladoa+ladoc and ladoa-ladob < ladoc < ladoa+ladob:
	perimetro = ladoa+ladob+ladoc
	print "Perimetro:", perimetro
else:
	area = ((ladoa + ladob) / 2) * ladoc
	print "Area:", area