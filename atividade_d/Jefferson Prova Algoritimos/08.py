valor1 = float(input('Informe o  primeiro valor: '))
valor2 = float(input('Informe o  segundo valor: '))
valor3 = float(input('Informe o  terceiro valor: '))
if (valor2 - valor3) * (-1) < valor1 and valor1 < valor2 + valor3:
	if (valor1 - valor3) * (-1) < valor2 and valor2 < valor1 + valor3:
		if (valor1 - valor2) * (-1) < valor3 and valor3 < valor1 + valor2:
			perimetro = float(valor1 + valor2 + valor3)
			print('Perimetro: %.1f' % perimetro)
		else:
			area = float(((valor1 + valor2)/2) * valor3)
			print('Area: %.1f' % area)
	else:
		area = float(((valor1 + valor2)/2) * valor3)
		print('Area: %.1f' % area)
else:
	area = float(((valor1 + valor2)/2) * valor3)
	print('Area: %.1f' % area)

