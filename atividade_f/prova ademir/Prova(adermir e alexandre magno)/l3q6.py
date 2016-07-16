def main():
	for i in range (1, 11):
		contador = 1
		print "Tabuada de %d:" %i
		while contador < 11:
			resultado = contador * i
			print contador, " x ", i, " = ", resultado
			contador = contador + 1

if __name__ == '__main__':
	main()