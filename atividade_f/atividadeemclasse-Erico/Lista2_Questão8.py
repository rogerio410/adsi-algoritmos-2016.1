def demonstrativo_pgto(valor_da_hora, horas_trabalhadas):
    salario_bruto = valor_da_hora * horas_trabalhadas
    print("Salário Bruto: (%.2f * %.2f)    :R$ %.2f"%(valor_da_hora, horas_trabalhadas, salario_bruto))
    if salario_bruto <= 900:
        print("(-) IR (ISENTO)")
        INSS = salario_bruto * 0.1
        print("(-) INSS (10%%)   :R$ %.2f"%INSS)
        sindicato = salario_bruto * 0.03
        print("(-) SINDICATO (3%%)   :R$ %.2f" %sindicato)
        FGTS = salario_bruto * 0.11
        print("FGTS (11%%)   :R$ %.2f" %FGTS)
        total_descontos = INSS + sindicato
        salario_liquido = salario_bruto - total_descontos
        print("Total de Descontos           :R$ %.2f" %total_descontos)
        print("Salário Liquido           :R$ %.2f" %salario_liquido)
    elif salario_bruto > 901 and salario_bruto <= 1500:
        IR = salario_bruto * 0.05
        print("(-) IR (5%%)  :R$ %.2f" % IR)
        INSS = salario_bruto * 0.1
        print("(-) INSS (10%%)   :R$ %.2f" % INSS)
        sindicato = salario_bruto * 0.03
        print("(-) SINDICATO (3%%)   :R$ %.2f" % sindicato)
        FGTS = salario_bruto * 0.11
        print("FGTS (11%%)   :R$ %.2f" % FGTS)
        total_descontos = INSS + sindicato + IR
        salario_liquido = salario_bruto - total_descontos
        print("Total de Descontos           :R$ %.2f" % total_descontos)
        print("Sal?rio Liquido           :R$ %.2f" % salario_liquido)

    elif salario_bruto > 1501 and salario_bruto <= 2500:
        IR = salario_bruto * 0.1
        print("(-) IR (10%%)   :R$ %.2f" % IR)
        INSS = salario_bruto * 0.1
        print("(-) INSS (10%%)   :R$ %.2f" % INSS)
        sindicato = salario_bruto * 0.03
        print("(-) SINDICATO (3%%)   :R$ %.2f" % sindicato)
        FGTS = salario_bruto * 0.11
        print("FGTS (11%%)   :R$ %.2f" % FGTS)
        total_descontos = INSS + sindicato + IR
        salario_liquido = salario_bruto - total_descontos
        print("Total de Descontos           :R$ %.2f" % total_descontos)
        print("Sal?rio Liquido           :R$ %.2f" % salario_liquido)
    else:
        IR = salario_bruto * 0.2
        print("(-) IR (20%%)   :R$ %.2f" % IR)
        INSS = salario_bruto * 0.1
        print("(-) INSS (10%%)   :R$ %.2f" % INSS)
        sindicato = salario_bruto * 0.03
        print("(-) SINDICATO (3%%)   :R$ %.2f" % sindicato)
        FGTS = salario_bruto * 0.11
        print("FGTS (11%%)   :R$ %.2f" % FGTS)
        total_descontos = INSS + sindicato + IR
        salario_liquido = salario_bruto - total_descontos
        print("Total de Descontos           :R$ %.2f" % total_descontos)
        print("Sal?rio Liquido           :R$ %.2f" % salario_liquido)


def main():
    valor_hora = float(input("Insira o valor da hora trabalhada, em R$: "))
    horas_trabalhadas = float(input("Insira o número de horas trabalhadas no mês: "))
    demonstrativo_pgto(valor_hora, horas_trabalhadas)

if __name__ == '__main__':
    main()