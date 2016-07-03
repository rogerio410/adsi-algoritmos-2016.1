def imprime_multiplos(numero):
    if numero + 1 == 11:
        return 'FIM'
    else:
        print numero
        multiplos = imprime_multiplos(numero,numero + 1)
        return 'Os 10 primeiros multiplos são: ', multiplos


def main():
    numero = input('Digite um numero: ')
    imprime_multiplos(numero)

if __name__ == '__main__':
    main()