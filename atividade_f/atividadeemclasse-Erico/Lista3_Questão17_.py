def soma_fracao(valorN):
    resultado = 0
    contador = 1
    valorN += 1
    for i in range(1, valorN):
        while contador < valorN:
            fracao = 1/contador
            print("1/%d ou %.2f" %(contador, fracao))
            resultado = resultado + fracao
            contador += 1
    print("%.2f"%resultado)


def main():
    valorN = int(input("Insira o valor limite para o denominador: "))
    print("S = ")
    soma_fracao(valorN)

if __name__ == '__main__':
    main()