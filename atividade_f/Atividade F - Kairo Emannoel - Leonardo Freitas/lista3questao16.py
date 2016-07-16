def fibonacci(n,numero1 = 0, numero2 = 1):
    if n>0:
        atual=numero1+numero2
        numero1=numero2
        numero2=atual
        print atual,
        fibonacci(n-1,numero1,numero2)

def main():
    n=input("Insira numero de termos: ")
    n-=2
    numero1=0
    numero2=1
    print numero1,numero2,
    fibonacci(n)

if __name__ == '__main__':
    main()