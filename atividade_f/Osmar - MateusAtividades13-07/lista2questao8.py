

def main():
    valor_hora = float(input("O valor da hora trabalhada em R$: "))
    qtd_horas = int(input("Quantidade de horas trabalhadas no mes: "))
    calcula_salario(valor_hora, qtd_horas)


def calcula_salario(valor_hora, qtd_horas):

    salario_bruto = valor_hora * qtd_horas
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    sindicato = salario_bruto * 0.03

    if salario_bruto <= 900.00:
        ir = 0.00
    elif salario_bruto <= 1500.00:
        ir = salario_bruto * 0.05
    elif salario_bruto <= 2500.00:
        ir = salario_bruto * 0.10
    else:
        ir = salario_bruto * 0.20

    descontos = ir + inss + sindicato
    salario_liquido = salario_bruto - descontos

    print(">>>>> Folha de Pagamento <<<<<")
    print("Salario Bruto: R$ ", salario_bruto)
    print("(-)IR (5%): R$ ", ir)
    print("(-)INSS (10%): R$ ", inss)
    print("(-)SINDICATO (3%): R$ ", sindicato)
    print("FGTS: R$ ", fgts)
    print("(-)DESCONTOS: R$ ",descontos)
    print("SALARIO LIQUIDO: R$ ", salario_liquido)




if __name__ == "__main__":
    main()