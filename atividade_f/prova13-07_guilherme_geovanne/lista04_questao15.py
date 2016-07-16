# Em Loop infinito.

def binario():
    n = 1

    bin = ''

    n = int(input("Numero na base decimal "))
    while  n >= 0:


        resto = n % 2
        n = n/2
        resul = bin + str(resto)

    print(resul)

if __name__ == '__main__':
    binario()
