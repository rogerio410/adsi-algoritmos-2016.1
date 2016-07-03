valor1 = input("valor A?")
valor2 = input("valor B?")
valor3 = input("valor C?")
valor4 = input("valor D?")
if (valor2 > valor3):
    if (valor4 > valor1):
        if(valor3 + valor4 > valor1 + valor2):
            if(valor3 > 0):
                if(valor4 > 0):
                    if(valor1 % 2 == 0):
                        print "valores aceitos"
else:
    print "valores nao aceitos"
