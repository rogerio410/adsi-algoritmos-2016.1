
def Questao13_Lista04(salario):

    salario_antigo_max = 0
    salario_novo_max = 0
    salario_antigo_max += salario
    
    while True:

        if salario == 0:

            print "Fim!"
            break
        
        if 0.0<= salario <= 2999.99:

            novo_salario = salario * 1.25
            salario_novo_max += novo_salario
            
        elif 3000.0<= salario <= 5999.99:

            novo_salario = salario * 1.20
            salario_novo_max += novo_salario

        elif 6000.0<= salario <= 9999.99:

            novo_salario = salario * 1.15
            salario_novo_max += novo_salario

        elif salario >= 10000.0:

            novo_salario = salario * 1.10
            salario_novo_max += novo_salario

        salario = input("Digite o proximo salario: ")
        salario_antigo_max += salario

    print "A soma de todos os antigos salarios foi igual a %.2f." % salario_antigo_max
    print "A soma de todos os novos salarios foi igual a %.2f." % salario_novo_max
    print "A diferenca entre os dois salarios foi igual a %.2f." % (salario_novo_max - salario_antigo_max)


def main():

    salario = input("Digite o salario: ")
    Questao13_Lista04(salario)

if __name__ == "__main__":

    main()
    
