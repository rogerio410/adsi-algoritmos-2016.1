#_*_ coding:utf-8 _*_
def calculo(n_pessoas):
    soma_salario=0.0
    numero_filhos=0.0
    pessoas_salario_maior_1000=0.0
    for i in range(n_pessoas):
        print "Habitante %d" % (i+1)
        salario=float(input("Insira o seu salário: "))
        n_filhos=float(input("Insira o seu número de filhos: "))

        soma_salario+=salario
        numero_filhos+=n_filhos

        if salario<=1000:
            pessoas_salario_maior_1000+=1

    print "Média salarial = R$ %.2f" % (soma_salario/n_pessoas)
    print "Média filhos = %.2f" % (numero_filhos/n_pessoas)
    print "Percentual de pessoas que ganham até R$ 1000,00 = %.2f por cento" % ((pessoas_salario_maior_1000/n_pessoas)*100.0)

def main():
    numero_de_habitantes=input("Insira o numero de habitantes: ")
    calculo(numero_de_habitantes)

if __name__ == '__main__':
    main()