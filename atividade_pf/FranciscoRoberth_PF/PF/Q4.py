def main():
	texto = ''
	entrada = raw_input('Digite um texto de no maximo 20 caracteres : ')
	tamanho_entrada = entrada
	while tamanho(tamanho_entrada) > 20:
		print ('Texto muito extenso!')
		entrada = raw_input('Digite um texto de no maximo 20 caracteres : ')
	for i in range(tamanho(tamanho_entrada)):
		print (' ' * i) + entrada[i]


def tamanho(valor):
    contador = 0
    for i in valor:
        contador += 1
    return contador

if __name__ == '__main__':
	main()