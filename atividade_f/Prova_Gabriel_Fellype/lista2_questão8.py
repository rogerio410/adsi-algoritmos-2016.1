# Estrutura if __name__
# IR Calculando errado.

nome_usuario = raw_input("Isira seu nome:")
valor_hora = input("valor da hora trabalhada:")
horas_trabalhadas = input("Quantidade de horas trabalhadas/mes:")
salario_bruto = valor_hora * horas_trabalhadas
salario_fgts = salario_bruto * 0.11
salario_total5_ir = salario_bruto - (salario_bruto * 0.10)
salraio_total5_inss = salario_bruto - (salario_bruto * 0.15)
salario_toal10_inss = salario_bruto - (salario_bruto * 0.10)
salario_total10_ir = salario_bruto - (salario_bruto * 0.15)
salario_total20_ir = salario_bruto - (salario_bruto * 0.25)
salario_toal20_inss = salario_bruto - (salario_bruto * 0.10)
inss = salario_bruto * 0.10
ir = salario_bruto * 0.05

if (salario_bruto <= 900):
    print "salario Bruto: $" , salario_bruto
    print "(-) IR(5%): $", ir
    print "(-)INSS(10%): $" ,inss
    print "FGTS(11%): $" ,salario_fgts
    print "Total de descontos: $" ,inss + ir
    print "Salario liquido: $" ,salario_bruto - (inss + ir)
if(salario_bruto >900 and salario_bruto <= 1500):
    print "salario Bruto: $" , salario_bruto
    print "(-) IR(5%): $", ir
    print "(-)INSS(10%): $" ,inss
    print "FGTS(11%): $" ,salario_fgts
    print "Total de descontos: $" ,inss + ir
    print "Salario liquido: $" ,salario_bruto - (inss + ir)
if(salario_bruto >1500 and salario_bruto <=2500):
    print "salario Bruto: $" , salario_bruto
    print "(-) IR(5%): $", ir
    print "(-)INSS(10%): $" ,inss
    print "FGTS(11%): $" ,salario_fgts
    print "Total de descontos: $" ,inss + ir
    print "Salario liquido: $" ,salario_bruto - (inss + ir)
if(salario_bruto >2500):
    print "salario Bruto: $" , salario_bruto
    print "(-) IR(5%): $", ir
    print "(-)INSS(10%): $" ,inss
    print "FGTS(11%): $" ,salario_fgts
    print "Total de descontos: $" ,inss + ir
    print "Salario liquido: $" ,salario_bruto - (inss + ir)
