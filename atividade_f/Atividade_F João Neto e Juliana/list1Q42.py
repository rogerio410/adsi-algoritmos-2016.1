def main():

	calculo()

def calculo():
	x1 = input("Digite x1:")
	y1 = input("Digite y1:")
	x2 = input("Digite x2:")
	y2 = input("Digite y2:")
	d =	((x2-x1)**2) + ((y2-y1)**2)
	calculo = d**0.5
	print "%2f" %(calculo)
 



if __name__ == '__main__':
	main()