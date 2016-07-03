def quest6():
  nome_vendedor = raw_input("Nome\n")
  salario_fixo = input("Salario Fixo\n")
  valor_total_vendas = input("Valor total de vendas\n")
  
  salario_total = salario_fixo + valor_total_vendas * 0.15
     
  print "Total a receber eh %.2f" % salario_total

def quest7():
  numero1 = input("Numero 1\n")
  numero2 = input("Numero 2\n")
  numero3 = input("Numero 3\n")
  numero4 = input("Numero 4\n")

  if numero2 > numero3 and numero4 > numero1 and (numero3 + numero4) > (numero1 + numero2) and numero3 > 0 and numero4 > 0 and numero1 % 2 == 0:
    print "Valores Aceitos\n"
  else:
    print "Valores nao aceito"  

def quest8():
  lado1 = input("Valor lado 1\n")
  lado2 = input("Valor lado 2\n")
  lado3 = input("Valor lado 3\n")
  
  if (lado2 - lado3) < lado1 and lado1 < (lado2 + lado3) and (lado1 - lado3) < lado2 and lado2 < (lado1 + lado3) and (lado1 - lado2) < lado3 and lado3 < (lado1 + lado2):
    perimetro = lado1 + lado2 + lado3
    print "perimetro = %.2f" % perimetro
  else:
    area_trapezio = (lado1 + lado2)/2 * lado3 
    print "Area = %.2f" %area_trapezio

    
if __name__ == '__main__':
   
 
	

