lado1_base1 = float(input("Insira o valor de A: "))
lado2_base2 = float(input("Insira o valor de B: "))
lado3_altura = float(input("Insira o valor de C: "))
if lado3_altura < lado1_base1 + lado2_base2 or lado2_base2 < lado1_base1 + lado3_altura \
		or lado1_base1 < lado2_base2 + lado3_altura:
	perimetro = lado1_base1 + lado2_base2 + lado3_altura
	print ("Perimetro = %.1f" % perimetro)
else: 
	print("O objeto descrito nao eh um triangulo")
	area = (((lado1_base1 + lado2_base2) * lado3_altura) / 2)
	print("Area = %.1f" % area)
