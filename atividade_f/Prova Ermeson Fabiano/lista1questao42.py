import math
def quest42_lista1():
    x1 = input("X1: ")
    x2 = input("X2: ")
    y1 = input("Y1: ")
    y2 = input("Y2: ")

    distancia = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)

    print "Distancia : %.2f" % distancia

def quest2_lista2():
    nota1 = input("Nota 1: ")
    nota2 = input("Nota 2: ")

    if (nota1 + nota2)/2 >= 7 and (nota1 + nota2)/2 < 10:
        print "Aprovado"
    elif (nota1 + nota2)/2 < 7:
        print "Reprovado"
    else:
        print "Aprovado com Distincao"

def quest8_lista2():
    horas_trabalhadas = input("Digite quantidade de horas trabalhadas: ")
    valor_hora = input("Digite o valor da hora trabalhada: ")
    IR = 0.0
    salario_bruto = horas_trabalhadas * valor_hora
    if salario_bruto <= 900:
        INSS = salario_bruto * 0.1
        FGTS = salario_bruto * 0.11
        Sindicato = salario_bruto * 0.03
    elif salario_bruto <= 1500:
        INSS = salario_bruto * 0.1
        FGTS = salario_bruto * 0.11
        Sindicato = salario_bruto * 0.03
        IR = salario_bruto * 0.05 
    elif salario_bruto <= 2500:
        INSS = salario_bruto * 0.1
        FGTS = salario_bruto * 0.11
        Sindicato = salario_bruto * 0.03
        IR = salario_bruto * 0.1
    else:
        INSS = salario_bruto * 0.1
        FGTS = salario_bruto * 0.11
        Sindicato = salario_bruto * 0.03
        IR = salario_bruto * 0.2

    print "Salario bruto: %.2f" %salario_bruto
    print "IR : %.2f" % IR
    print "INSS : %.2f" % INSS
    print "FGTS : %.2f" % FGTS
    print "Total de descontos : %.2f" % (IR + INSS + Sindicato)
    print "Salario Liquido : %.2f" % (salario_bruto - (IR + INSS + Sindicato))
    

def quest17_lista3():
    Numero_n = input("Numero N : ")
    soma = 0
    cont = 1
    

    for i in range(1, Numero_n + 1):
        soma += 1/float(i)
    

    print "soma = %.2f" % soma

def quest24_lista3():
    numero = input("Voce quer inserir as informacoes de quantos habitantes? ")
    lista = range(numero)
    salariototal = 0
    filhostotal = 0
    pessoassalario1000 = 0
    for i in lista:
        salario = input("Qual e o salario dele? ") 
        filhos = input("Quantos filhos ele tem? ")
        salariototal+= salario
        filhostotal+= filhos
        if salario > 1000:
            pessoassalario1000+= 1
    print "Media de salario da populacao eh de %.1f." %(salariototal / float(numero))
    print "Media de numero de filho eh de %.1f" %(filhostotal / float(numero))
    print "Percentual de pessoas ganhando mais de 1000 reais eh de %.1f" %((pessoassalario1000 / float(numero) * 100))

def quest13_lista4():
    soma_S = 0
    soma_Sreajustado = 0
    salario = 1
    while 1 == 1:
        salario = input("Digite salario: ")
        if salario == 0:
            break
        if salario <= 2999.99:
            salario_reajustado = salario * 1.25
            soma_S += salario
            soma_Sreajustado += salario_reajustado
        
        elif salario <= 5999.99:
            salario_reajustado = salario * 1.2
            soma_S += salario
            soma_Sreajustado += salario_reajustado

        elif salario <= 9999.99:
            salario_reajustado = salario * 1.15
            soma_S += salario
            soma_Sreajustado += salario_reajustado

        else:
            salario_reajustado = salario * 1.1
            soma_S += salario
            soma_Sreajustado += salario_reajustado

    print "Soma dos salarios atuais : %.2f" % soma_S
    print "Soma dos salarios reajustado : %.2f" % soma_Sreajustado
    print "Diferenca entre as duas somas : %.2f" % (soma_Sreajustado - soma_S)

def quest15_lista4():
    Numero = input("Numero de 1 a 254: ")
    besta = 100000000
    print "Resultado eh esse numero ao contrario"
    cont = 1
    for i in range(8):
        besta += (Numero % 2) * cont
        Numero /= 2 
        cont *= 10            
    print "%d" %(besta - 100000000)
def quest23_lista4():
    numero = input("Digite primeiro: ")
    limite = input("Digite quantidade de termos: ")
    razao = input("Digite a razao: ")
    print("Progressao Geometrica:")
    
    for i in range(limite):
        print("%d"%numero)
        numero *= razao

def quest24_lista4():
    numero = input("Digite primeiro: ")
    limite = input("Digite quantidade de termos: ")
    razao = input("Digite a razao: ")
    print("Progressao Aritmetica:")
    
    for i in range(limite):
        print("%d"%numero)
        numero += razao

def main():
    quest15_lista4()

if __name__ == '__main__':
    main()