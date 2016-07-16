
def main():
    primeira_nota, segunda_nota = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))
    media = (primeira_nota + segunda_nota) / 2
    print(analisa_media(media))

def analisa_media(media):
    if media >= 7.0 and media < 10.0:
        return "Aprovado!"
    elif media == 10.0:
        return "Aprovado com Distincao!"
    else:
        return "Reprovado!"

if __name__ == "__main__":
    main()