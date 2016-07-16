''' Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
 (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.  
Leia N, calcule e escreva o valor de S. '''


#Recursiva porem imprimindo erradamente a qtd de elementos.

def main():
	while True:
		anterior_1 = 0
		anterior_2 = 1
		cont = 0
		n = int(input('digite um numero: '))
		if(n<2):
			print('Digite um numero maior ou igual a dois!!!')
		elif(n == 2):
			print(0, 1)
			break
		else:
			fibonacci(n,anterior_1,anterior_2,cont)
			break


def fibonacci(n,anterior_1,anterior_2,cont):
	cont += 1
	if(cont <= n):
		print(anterior_1,anterior_2)
		fibonacci(n,anterior_1+anterior_2 ,anterior_1+(anterior_2 * 2),cont)

if __name__ == '__main__':
	main()