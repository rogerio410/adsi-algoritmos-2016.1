
def main():
    numero = int(input("Digite o total de termos da PG: "))
    primeiro_termo = int(input("Qual o primeiro termo da PG: "))
    razao = int(input("Digite o valor da razao da PG: "))
    escreva_termos(numero, primeiro_termo, razao)


def escreva_termos(numero, primeiro_termo, razao):
    print(">>>> SEQUENCIA DE TERMOS <<<<")
    for i in range(numero):
        print(primeiro_termo)
        primeiro_termo = primeiro_termo + razao


if __name__ == "__main__":
    main()