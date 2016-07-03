#developed by Kairo_Costa
def condicao_valores(a,b,c,d):
	if (b>c) and (d>a) and ((c+d)>(a+b)) and (c>0 and d>0) and (a%2==0):
		print "Valores aceitos"
	else:
		print "Valores nao aceitos"

def main():
	a=input("Insira valor de A: ")
	b=input("Insira valor de B: ")
	c=input("Insira valor de C: ")
	d=input("Insira valor de D: ")
	condicao_valores(a,b,c,d)

if __name__=="__main__":
	main()
