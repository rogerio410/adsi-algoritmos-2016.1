def main():
	qtd = input()

	for i in range(qtd):
		qtd_alunos = input()
		alunos = raw_input().split(' ')
		frequencias = raw_input().split(' ')

		for j in range(len(alunos)):
			p = frequencias[j].count('P')
			a = frequencias[j].count('A')
			freq = p / float(a + p)
			if (freq < 0.75):
				print alunos[j],

		print '\n'

if __name__ == '__main__':
	main()