#atividade 10
#29/06 - jhonatan matheus

def tabuada(numero_recebido, contador_recebido):
        i = contador_recebido
        total = 0
        for i in range(10-contador_rebido, 1):
            total = numero_recebido * i
            print("%d * %d = %d"%(numero_recebido, i, total))

if __name__ == '__main__':
    numero = int(input("Digite um numero inteiro: "))
    contador = int(input("Digite um numero inteiro para multiplicar apartir dele: "))
    tabuada(numero, contador)
