reajuste_total = 0
salario = 1
salario_total = 0
while salario != 0:
	salario = input("Salario: ") 
	if salario <= 2999.99:
		salario_total += salario
		reajuste = salario + (salario * 0.25)
		reajuste_total += reajuste
	elif 3000.00 <= salario <= 5999.99:
		salario_total += salario
		reajuste = salario + (salario * 0.20)
		reajuste_total += reajuste
	elif 6000.00 <= salario <= 9999.99:
		salario_total += salario
		reajuste = salario + (salario * 0.15)
		reajuste_total += reajuste
	elif salario >= 10000.00:
		salario_total += salario
		reajuste = salario + (salario * 0.10)
		reajuste_total += reajuste


print "Total: %.2f" % salario_total
print "Reajustado : %.2f" % reajuste_total
print "Diferenca : %.2f" % (reajuste_total - salario_total)

