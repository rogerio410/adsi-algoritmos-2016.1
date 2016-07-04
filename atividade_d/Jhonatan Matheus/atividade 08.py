#8question
#29/06 - jhonatan matheus

def triangulo(a, b, c):
    if(((int(b-c)) < a < b+c)and((int(a-c)) < b < a+c)and((a-b) < c < a+b)):
        perimetro = a+b+c
        print(perimetro)
    else:
        area = (a+b)*c
        print(area)

if __name__ == '__main__':
    a = int(input("Digite um valor para \'a\': "))
    b = int(input("Digite um valor para \'b\': "))
    c = int(input("Digite um valor para \'c\': "))

    triangulo(a, b, c)
