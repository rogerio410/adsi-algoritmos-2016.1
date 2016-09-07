def main():
	texto = raw_input('Digite um texto de no maximo 20 caracteres: ')
	while len(texto) > 20:
		texto = raw_input('Texto muito extenso!\nDigite um texto de no maximo 20 caracteres: ')
	for i in range(len(texto)):
		print ' ' * i + texto[i]

if __name__ == '__main__':
	main()