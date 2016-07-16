
def Questao08_Lista02(valor_hora, total_horas):
    salario_bruto = valor_hora*total_horas
    
    if salario_bruto <= 900.0:
        
        print "Contribuinte isento de IRPF."
        
    elif salario_bruto > 900.0 and salario_bruto <= 1500.0:

        IR = 5
        imposto_renda = 0.05 * salario_bruto
        inss = 0.10 * salario_bruto
        fgts = 0.11 * salario_bruto
        sindicato = 0.03 * salario_bruto
        salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

        print "Salario Bruto: (%.2f * %d): R$ %.2f." % (valor_hora, total_horas, salario_liquido)
        print "(-) IR (%d%%) :R$ %.2f. " % (IR, imposto_renda)
        print "(-)  INSS (10 %%): R$ %.2f. " % inss
        print "Contribuicao Sindical (3 %%): R$ %.2f. " % sindicato
        print "FGTS (11 %%): R$ %.2f. " % (fgts)
        print "Total de descontos: R$ %.2f." % (imposto_renda + inss + sindicato)
        print "Salario liquido: R$ %.2f." % salario_liquido

    elif salario_bruto > 1500.0 and salario_bruto <= 2500.0:

        IR = 10
        imposto_renda = 0.10 * salario_bruto
        inss = 0.10 * salario_bruto
        fgts = 0.11 * salario_bruto
        sindicato = 0.03 * salario_bruto
        salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

        print "Salario Bruto: (%.2f * %d): R$ %.2f." % (valor_hora, total_horas, salario_liquido)
        print "(-) IR (%d%%) :R$ %.2f. " % (IR, imposto_renda)
        print "(-)  INSS (10 %%): R$ %.2f. " % inss
        print "Contribuicao Sindical (3 %%): R$ %.2f. " % sindicato
        print "FGTS (11 %%): R$ %.2f. " % (fgts)
        print "Total de descontos: R$ %.2f." % (imposto_renda + inss + sindicato)
        print "Salario liquido: R$ %.2f." % salario_liquido

    elif salario_bruto > 2500.0:

        IR = 20
        imposto_renda = 0.20 * salario_bruto
        inss = 0.10 * salario_bruto
        fgts = 0.11 * salario_bruto
        sindicato = 0.03 * salario_bruto
        salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

        print "Salario Bruto: (%.2f * %d): R$ %.2f." % (valor_hora, total_horas, salario_liquido)
        print "(-) IR (%d%%) :R$ %.2f. " % (IR, imposto_renda)
        print "(-)  INSS (10 %%): R$ %.2f. " % inss
        print "Contribuicao Sindical (3 %%): R$ %.2f. " % sindicato
        print "FGTS (11 %%): R$ %.2f. " % (fgts)
        print "Total de descontos: R$ %.2f." % (imposto_renda + inss + sindicato)
        print "Salario liquido: R$ %.2f." % salario_liquido





def main():
    valor_hora = input("Digite o valor pago por hora do seu trabalho: ")
    total_horas = input("Digite quantas horas voce trabalhou por mes: ")
    Questao08_Lista02(valor_hora, total_horas)


if __name__ == "__main__":

    main()
    
    
