print 'Programa questao 7'
def ver_num (a, b, c, d):
	if (b>c) and (d>a) and ((c+d) > (a+b)) and (c>0) and (d>0) and (a%2==0):
		return 'Valores aceitos'
	else:
		return 'valores nao aceitos'

def main():
	a = input('Digite um numero equivalente a A:\n')
	b = input('Digite um numero equivalente a B:\n')
	c = input('Digite um numero equivalente a C:\n')
	d = input('Digite um numero equivalente a D:\n')
	fun = ver_num(a, b, c, d)

if __name__ == '__main__':
	main()