#_*_ coding:utf-8 _*_
def calculo_salarial(actual_value):
    if actual_value<3000.00:
        bonus=(actual_value/100.0)*25
        return actual_value+bonus
    elif actual_value<6000.00:
        bonus=(actual_value/100.0)*20
        return actual_value + bonus
    elif actual_value<10000.00:
        bonus=(actual_value/100.0)*15
        return actual_value + bonus
    else:
        bonus=(actual_value/100.0)*10
        return actual_value+bonus


def main():
    salario=input("Insira salário do Funcionário: ")
    soma_salarios_atuais=0
    soma_salarios_reajustados = 0
    while salario>0:
        print calculo_salarial(salario)
        soma_salarios_atuais+=salario
        salario_novo=calculo_salarial(salario)
        soma_salarios_reajustados+=salario_novo
        salario=input("Insira salário do Funcionário: ")

    print "Soma Salários atuais = R$%.2f" % (soma_salarios_atuais)
    print "Soma Salários reajustados = R$%.2f" % (soma_salarios_reajustados)
    print "Diferença após o reajuste = R$%.2f" % (soma_salarios_reajustados-soma_salarios_atuais)

if __name__ == '__main__':
    main()