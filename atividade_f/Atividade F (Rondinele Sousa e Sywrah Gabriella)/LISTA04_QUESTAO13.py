# -*- coding: utf-8 -*-
"""
13. Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios descritos abaixo),
a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2 somas. (Flag: salário=0)
"""

def main ():
    salario = input('Digite o salário do funcionário: ')
    salario_novo = 0
    soma_salarios = 0
    soma_salarios_novo = 0
    while salario != 0:
        if salario < 3000:
            salario_novo = salario * 1.25
        elif salario < 6000:
            salario_novo = salario * 1.2
        elif salario < 10000:
            salario_novo = salario * 1.15
        else:
            salario_novo = salario * 1.1
        print 'O salário alterou de R$ %.2f para R$ %.2f' %(salario, salario_novo)
        soma_salarios = soma_salarios + salario
        soma_salarios_novo = soma_salarios_novo + salario_novo
        salario = input('Digite o salário do próximo funcionário: ')

    print 'Soma dos salários antigos: R$ %.2f' % soma_salarios
    print 'Soma dos salários novos: R$ %.2f' % soma_salarios_novo
    print 'Diferença: R$ %.2f' % (soma_salarios_novo - soma_salarios)


if __name__ == '__main__':
    main()
