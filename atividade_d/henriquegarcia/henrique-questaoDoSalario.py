# _*_coding:utf-8_*_
# Questão que pedia o salário total do vendedor com a comissão das vendas

def salario_total(salario_fixo, total_de_vendas):
    salario_total = (salario_fixo + (total_de_vendas * 0.15))
    return("Seu salario é igual a R$ %.2f" % salario_total)


def main():
    nome = raw_input("Digite seu nome: ")
    salario_fixo = input("Digite seu salário fixo: ")
    total_de_vendas = input("Digite o seu total de vendas em dinheiro: ")
    salario_total(salario_fixo, total_de_vendas)
    print(salario_total(salario_fixo, total_de_vendas))

if __name__ == '__main__':
    main()
