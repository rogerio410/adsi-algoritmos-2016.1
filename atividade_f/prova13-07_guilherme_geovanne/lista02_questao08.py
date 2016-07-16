
# Alguns Calculos Errados. Como para pessoas com salario ate 900 reais.
def imposto():

    salario_liqido = 0

    valor_da_hora = float(input("valor p/hora "))
    qtd_horas = int(input("quantidade/horas "))

    salario_bruto = valor_da_hora*qtd_horas


    print("Salario bruto R$ %.2f"%salario_bruto)

    if salario_bruto <= 900.0:
        print("isento ")

    elif salario_bruto > 900.0 and salario_bruto <= 1500.0:
        ir = salario_bruto * 0.05
        inss = salario_bruto * 0.10
        fgts = salario_bruto * 0.11
        sindicato = salario_bruto* 0.03
        descontos = ir + inss + sindicato
        salario_liquido = salario_bruto - descontos
        print("-IR(5) %.2f"%ir)
        print("-IR(10)%.2f"%inss)
        print("-FGTS(11)%.2f"%fgts)
        print("-Sindicato(3)%.2f"%sindicato)
        print("Total de desconto %.2f"%descontos)
        print("salario liquido %.2f"%salario_liquido)
    elif salario_bruto > 1500.0  and salario_bruto <= 2500.0:
        ir = salario_bruto * 0.10
        inss = salario_bruto * 0.10
        fgts = salario_bruto * 0.11
        sindicato = salario_bruto* 0.03
        descontos = ir + inss + sindicato
        salario_liquido = salario_bruto - descontos
        print("-IR(5) %.2f"%ir)
        print("-IR(10)%.2f"%inss)
        print("-FGTS(11)%.2f"%fgts)
        print("-Sindicato(3)%.2f"%sindicato)
        print("Total de desconto %.2f"%descontos)
        print("salario liquido %.2f"%salario_liquido)


    elif salario_bruto > 2500.0:
        ir = salario_bruto * 0.20
        inss = salario_bruto * 0.10
        fgts = salario_bruto * 0.11
        sindicato = salario_bruto* 0.03
        descontos = ir + inss + sindicato
        salario_liquido = salario_bruto - descontos
        print("-IR(5) %.2f"%ir)
        print("-IR(10)%.2f"%inss)
        print("-FGTS(11)%.2f"%fgts)
        print("-Sindicato(3)%.2f"%sindicato)
        print("Total de desconto %.2f"%descontos)
        print("salario liquido %.2f"%salario_liquido)


def main():
    imposto()


if __name__ == '__main__':
    main()
