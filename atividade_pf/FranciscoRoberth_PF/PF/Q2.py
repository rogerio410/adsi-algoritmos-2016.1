def main():
	emprestimo = 3000.00
	pagamento = 200.00
	contador = 0
	while emprestimo > 0:
		emprestimo = emprestimo - pagamento
		emprestimo = emprestimo + (emprestimo * 0.0085)
		contador += 1
		if contador % 5 == 0:
			emprestimo = emprestimo + (emprestimo * 0.0085)
			emprestimo = emprestimo + (emprestimo * 0.0085)
	print 'A quantidade de dias necessarios para pagar o emprestimo eh de: %d dias.' %(contador)
if __name__ == '__main__':
	main()