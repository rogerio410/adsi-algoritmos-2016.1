valor_A, valor_B = int(input("Digite o valor A: ")), int(input("Digite o valor B: "))
valor_C, valor_D = int(input("Digiteo valor C: ")), int(input("Digite o valor D: "))
if valor_B > valor_C and valor_D > valor_A and (valor_C + valor_D) > (valor_A + valor_B) and (valor_C, valor_D) >= 0:
	print "Valores aceito"
else:
	print "Valores nao aceito"