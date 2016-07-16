#_*_ coding:utf-8 _*_
def calculo_media(nota1,nota2):
    media=(nota1+nota2)/2.0
    if media == 10.0:
        print "Aprovado com Distinção"

    elif media >= 7:
        print "Aprovado"

    else:
        print "Reprovado"

def main():
    nota1 = input("Insira primeira nota: ")
    nota2 = input("Insira segunda nota: ")
    calculo_media(nota1,nota2)

if __name__ == '__main__':
    main()