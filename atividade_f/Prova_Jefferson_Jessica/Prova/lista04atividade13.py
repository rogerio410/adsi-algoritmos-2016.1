'''Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
somas. (Flag: salário=0)'''

def main():
    salario = 1
    while salario != 0:
        salario = float(input('Informe o seu salário: '))
        if salario >= 0 and salario < 3000.00:
            aumento = salario * 0.25
            novo_salario = salario + aumento
            print('Seu novo salário é: %.2f' % novo_salario)
        elif salario >= 3000.00 and salario < 6000.00:
            aumento = salario * 0.20
            novo_salario = salario + aumento
            print('Seu novo salário é: %.2f' % novo_salario)
        elif salario >= 6000.00 and salario < 10000.00:
            aumento = salario * 0.15
            novo_salario = salario + aumento
            print('Seu novo salário é: %.2f' % novo_salario)
        else:
            aumento = salario * 0.10
            novo_salario = salario + aumento
            print('Seu novo salário é: %.2f' % novo_salario)
    print('FIM')


if __name__ == '__main__':
    main()