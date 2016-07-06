valor_a = input("Valor A:")
valor_b = input("Valor B:")
valor_c = input("Valor C:")
modulo_vb_eVc = valor_b - valor_c
sub_mod = modulo_vb_eVc*modulo_vb_eVc/modulo_vb_eVc
perimetro = valor_a + valor_b + valor_c
area_trapezio = ((valor_a+valor_b)/2)*valor_c
modulo_va_eVc = valor_a - valor_c
sub_mod2 = modulo_va_eVc*modulo_va_eVc/modulo_va_eVc
modulo_va_eVb = valor_a - valor_b
sub_mod3 = modulo_va_eVb*modulo_va_eVb/modulo_va_eVb

if sub_mod < valor_a < valor_b + valor_c:
	print"Atende a condicao 1 :perimetro:", perimetro
else: 
	print "Nao atende a condicao 1 :Area do trapezio", area_trapezio 

if sub_mod2 < valor_b < valor_a +valor_c:
	print"Atende a condicao 2 :perimetro:", perimetro
else: 
	print "Nao atende a condicao 2:Area do trapezio", area_trapezio 

if sub_mod3 < valor_c < valor_a + valor_b:
	print"Atende a condicao 3 :perimetro:", perimetro
else: 
	print "Nao atende a condicao 3:Area do trapezio", area_trapezio 