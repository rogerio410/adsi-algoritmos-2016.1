

def main():
    total = 0
    limite = int(input('Informe um limite: '))
    for denominador in range (1, limite +1):
        s = 1/denominador
        total += s
        print('1/{} + '.format(denominador))
    print('O resultado da soma de todas as frações é: %.2f ' % total)


if __name__ == '__main__':
    main()