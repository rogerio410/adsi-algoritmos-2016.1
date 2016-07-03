def triangulo (a, b, c):
	if ((b-c) < a < (b+c)) and  ((a-c)< b < (a+c)) and ((a-b) < c < (a+b)):
		per = (a+b+c)
		return 'O perimetro e %.1f' %(per)
	else:
		area = ((a+b)*c)/2
		return 'A area do trapezio e %.1f' %(area) 

def main():
	print ('Insira os tres lados do triangulo e pressione ENTER:\n')
	a, b, c = input(), input(), input()
	fun = triangulo (a, b, c)
	print (fun)

if __name__ == '__main__':
	main()