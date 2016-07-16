def sequencia_fibonacci(limite_sequencia):
    print(limite_sequencia)
    if limite_sequencia > 0:
        primeiro_termo = 0
        segundo_termo = 1
        termo_auxiliar = primeiro_termo + segundo_termo
        print(termo_auxiliar)
        primeiro_termo = segundo_termo
        segundo_termo = termo_auxiliar
        sequencia_fibonacci(limite_sequencia - 1)


def main():
    limite_sequencia = int(input("Insira o limite da sequencia: "))
    print(0)
    print(1)
    sequencia_fibonacci(limite_sequencia)

if __name__ == '__main__':
    main()