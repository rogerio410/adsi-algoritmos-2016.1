#developed by Kairo_Costa
def condicao(a,b,c):
	if (((b-c)*-1) < a and a < (b+c)) and (((a-c)*-1) < b and b < (a+c)) and ((a-b)*-1) < c and c < (a+b):
		print "Perimetro = %.1f" % (a+b+c)
	else:
		print "Area do Trapezio = %.1f" % (((a+b)*c)/2)

def main():
	a=input("Insira o A: ")
	b=input("Insira o B: ")
	c=input("Insira o C: ")
	condicao(a,b,c)

if __name__=="__main__":
	main()
