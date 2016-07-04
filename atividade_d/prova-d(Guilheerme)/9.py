#Escreva um programa que receba um numero inteiro e
#que recursivamente escreva os seus 10 primeiros multiplos.

def multiplo(numero):
    if numero==0:
        return 1
    else:
        if numero%2 == 0:
            print(numero)
            print(multiplo(numero+1))
            #return numero + 1
        else:
            return numero

multiplo(1000)

