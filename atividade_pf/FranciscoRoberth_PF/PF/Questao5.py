def main():
    palavra = raw_input('Digite o texto: ')
    posicao = input('Digite a chave: ')
    opcao = input('Digite 1 para Criptografar ou 2 para descriptografar: ')
    if opcao == 1:
        cifra_de_cesar(palavra,posicao)
    elif opcao == 2:
        cifra_reversa(palavra,posicao)
def cifra_de_cesar(palavra,posicao):
    cifra_cesar = ''
    for j in palavra:
        if (j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z'):
            if j >= 'a' and j <= 'z':
                cifra = (ord(j) - ord('a') + posicao) % 26
                cifra_cesar += chr(cifra + ord('a'))
            else:
                cifra = (ord(j) - ord('A') + posicao) % 26
                cifra_cesar += chr(cifra + ord('A'))
        else:
            cifra_cesar += j
    print cifra_cesar

def cifra_reversa(palavra,posicao):
    cifra_cesar = ''
    for j in palavra:
        if (j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z'):
            if j >= 'a' and j <= 'z':
                cifra = (ord(j) - ord('a') - posicao) % 26
                cifra_cesar += chr(cifra + ord('a'))
            else:
                cifra = (ord(j) - ord('A') - posicao) % 26
                cifra_cesar += chr(cifra + ord('A'))
        else:
            cifra_cesar += j
    print cifra_cesar

if __name__ == '__main__':
    main()