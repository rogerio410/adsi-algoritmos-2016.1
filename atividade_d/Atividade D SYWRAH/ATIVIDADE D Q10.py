def imprime_tabuada(numero1, numero2):
    if numero2 == 11:
        return 'FIM'
    else:
        resultato = numero1 * numero2
        print numero1, 'x', numero2, '=', resultato
        resultado2 = imprime_tabuada(numero1, numero2 + 1)
        return numero1, 'x', numero2, '=', resultado2


def main():
    numero1 = input('Qual tabuada voce deseja? ')
    numero2 = input ('Digite o numero pelo qual deseja comecar: ')
    imprime_tabuada(numero1,numero2)

if __name__ == '__main__':
    main()