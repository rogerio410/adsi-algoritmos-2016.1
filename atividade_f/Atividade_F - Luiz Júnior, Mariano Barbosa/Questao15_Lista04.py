#Errada
def Questao15_Lista04(base_decimal):

    binario = ""
    numero = 1
    if 0 <= base_decimal <= 255:

        while numero!=128:

            if base_decimal%numero==0:
                         
                binario += "1"
                base_decimal = base_decimal%numero
                
            else:

                binario += "0"
            numero *= 2
            
            
    print "O binario foi igual a %s." % binario
                

            
        


def main():

    decimal = input("Digite o valor decimal a ser convertido em binario: ")
    Questao15_Lista04(decimal)

if __name__ == "__main__":

    main()
