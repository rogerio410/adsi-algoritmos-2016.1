#Esqueceu o sindicato
#_*_ coding:utf-8 _*_
def calculo_salario(salario_bruto):
    if salario_bruto<=900.00:
        print "Salário Bruto: R$%.2f" % (salario_bruto)
        #isento
        imposto_de_renda=0
        print "IR = Isento"
        inss=(salario_bruto*10)/100.0
        print "INSS: R$%.2f" % inss
        fgts=(salario_bruto*11)/100
        print "FGTS: R$%.2f" % (fgts)
        total_impostos=imposto_de_renda+inss
        print "Total de Descontos: R$%.2f" % (total_impostos)
        salario_liquido=salario_bruto-total_impostos
        print "Salário Líquido: R$%.2f" % (salario_liquido)

    elif salario_bruto<=1500.00:
        print "Salário Bruto: R$%.2f" % (salario_bruto)
        imposto_de_renda=(salario_bruto*5)/100.0
        print "IR: R$%.2f" % (imposto_de_renda)
        inss=(salario_bruto*10)/100
        print "INSS: R$%.2f" % inss
        fgts=(salario_bruto*11)/100
        print "FGTS: R$%.2f" % (fgts)
        total_impostos=imposto_de_renda+inss
        print "Total de Descontos: R$%.2f" % (total_impostos)
        salario_liquido=salario_bruto-total_impostos
        print "Salário Líquido: R$%.2f" % (salario_liquido)

    elif salario_bruto<=2500.00:
        print "Salário Bruto: R$%.2f" % (salario_bruto)
        imposto_de_renda=(salario_bruto*10)/100.0
        print "IR: R$%.2f" % (imposto_de_renda)
        inss=(salario_bruto*10)/100
        print "INSS: R$%.2f" % inss
        fgts=(salario_bruto*11)/100
        print "FGTS: R$%.2f" % (fgts)
        total_impostos=imposto_de_renda+inss
        print "Total de Descontos: R$%.2f" % (total_impostos)
        salario_liquido=salario_bruto-total_impostos
        print "Salário Líquido: R$%.2f" % (salario_liquido)

    else:
        print "Salário Bruto: R$%.2f" % (salario_bruto)
        imposto_de_renda=(salario_bruto*20)/100.0
        print "IR: R$%.2f" % (imposto_de_renda)
        inss=(salario_bruto*10)/100
        print "INSS: R$%.2f" % inss
        fgts=(salario_bruto*11)/100
        print "FGTS: R$%.2f" % (fgts)
        total_impostos=imposto_de_renda+inss
        print "Total de Descontos: R$%.2f" % (total_impostos)
        salario_liquido=salario_bruto-total_impostos
        print "Salário Líquido: R$%.2f" % (salario_liquido)

def main():
    value_hour=input("Insira valor da Hora: ")
    number_hour=input("Insira número de horas trabalhadas: ")
    salario_bruto=value_hour*number_hour
    calculo_salario(salario_bruto)

if __name__ == '__main__':
    main()