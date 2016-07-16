def main():
	primeiro_termo = input("Digite o primeiro termo: ")
	razao = input("Digite a razao: ")
	valor_n = input("Digite a quantidade N: ")
	contador = 1
	resultado = primeiro_termo * razao
	print resultado
	while contador < valor_n:
		resultado = resultado * razao
		print resultado
		contador += 1
if __name__ == '__main__':
	main()